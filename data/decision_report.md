# Decision Report

- generated_at: 2026-09-16T10:41:33.153058+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14664**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14664, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.44%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.44% | **-0.44%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 10/20 | 50.0% | +2.08% | **+1.04%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.62% | **+0.40%** |
| LIMIT_ATR | 15/20 | 75.0% | +0.39% | **+0.29%** |
| LIMIT_7PCT | 5/20 | 25.0% | +1.12% | **+0.28%** |
| LIMIT_6PCT | 5/20 | 25.0% | -0.47% | **-0.12%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 6/9 | 66.7% | +3.14% | **+2.10%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.47% | **+1.25%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +2.41% | **+0.60%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.68% | **+0.48%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +0.73% | **+0.44%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 214件 (TP 79 / SL 130 / EXP 5)
- 最新: SHROOM/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,048.07** / 初期 $100.00 (+948.07%)
- 確定: 5542件 (Win 1651 / Loss 1791 / Flat 2100) / skip 5683件
- 成長率目線: 平均log +0.000424 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BR/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $1,048.07

## 4. Robust Adaptive DryRun ($100)

- 残高: **$230.42** / 初期 $100.00 (+130.42%)
- 確定: 3070件 (Win 843 / Loss 722 / Flat 1505) / skip 5005件
- 成長率目線: 平均log +0.000272 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0290 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BR/USDT:USDT `LIMIT_5PCT` TP_HIT account +0.69% 残高後 $230.42

## 5. Causal Adaptive DryRun ($100)

- 残高: **$124.18** / 初期 $100.00 (+24.18%)
- 確定: 2953件 (Win 878 / Loss 1162 / Flat 913) / pending 3件 / skip 3179件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000183 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BR/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $124.18

## 6. Latest Market Context

- 更新: 2026-09-16T10:41:17.498079+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=75941.6
- Funnel: target 1058 → liquid 154 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 73.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SYN/USDT:USDT | +108.70% | $16,747,259.96 |
| BR/USDT:USDT | +39.50% | $17,618,027.64 |
| LSK/USDT:USDT | +30.80% | $21,872,853.53 |
| USELESS/USDT:USDT | +14.79% | $7,418,657.54 |
| LONGXIA/USDT:USDT | +13.44% | $2,663,757.32 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKYAI/USDT:USDT | below_1h_threshold | +3.25% | +3.27% |
| 4/USDT:USDT | below_1h_threshold | +2.03% | +2.06% |
| AKE/USDT:USDT | below_1h_threshold | +1.65% | +1.67% |
| LONGXIA/USDT:USDT | below_1h_threshold | +0.99% | +1.01% |
| MARSCOIN/USDT:USDT | below_1h_threshold | +0.59% | +0.62% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
