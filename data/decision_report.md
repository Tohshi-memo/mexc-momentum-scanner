# Decision Report

- generated_at: 2026-09-16T10:51:38.040655+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14665**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14665, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.04%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.04% | **-1.04%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 10/20 | 50.0% | +2.08% | **+1.04%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.57% | **+0.40%** |
| LIMIT_ATR | 16/20 | 80.0% | +0.36% | **+0.29%** |
| LIMIT_7PCT | 5/20 | 25.0% | +1.12% | **+0.28%** |
| LIMIT_6PCT | 5/20 | 25.0% | -0.47% | **-0.12%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 6/10 | 60.0% | +3.14% | **+1.89%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +2.01% | **+1.70%** |
| MARKET_LONG | 20/20 | 100.0% | +0.79% | **+0.79%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.04% | **+0.68%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +1.16% | **+0.64%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 214件 (TP 79 / SL 130 / EXP 5)
- 最新: SHROOM/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,048.07** / 初期 $100.00 (+948.07%)
- 確定: 5543件 (Win 1651 / Loss 1791 / Flat 2101) / skip 5683件
- 成長率目線: 平均log +0.000424 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BR/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.00% 残高後 $1,048.07

## 4. Robust Adaptive DryRun ($100)

- 残高: **$230.42** / 初期 $100.00 (+130.42%)
- 確定: 3071件 (Win 843 / Loss 722 / Flat 1506) / skip 5005件
- 成長率目線: 平均log +0.000272 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0290 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BR/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $230.42

## 5. Causal Adaptive DryRun ($100)

- 残高: **$123.97** / 初期 $100.00 (+23.97%)
- 確定: 2954件 (Win 878 / Loss 1163 / Flat 913) / pending 2件 / skip 3182件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000172 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BR/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $123.97

## 6. Latest Market Context

- 更新: 2026-09-16T10:51:19.505208+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=75921.8
- Funnel: target 1058 → liquid 154 → pre 50 → checked 50 → surge 3 → strict 3
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SYN/USDT:USDT | +114.70% | $17,202,794.66 |
| BR/USDT:USDT | +43.63% | $18,589,178.88 |
| LSK/USDT:USDT | +40.50% | $22,520,313.88 |
| USELESS/USDT:USDT | +16.63% | $7,463,937.36 |
| LONGXIA/USDT:USDT | +14.39% | $2,673,181.53 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CNPY/USDT:USDT | below_1h_threshold | +4.95% | +5.00% |
| SKYAI/USDT:USDT | below_1h_threshold | +4.81% | +4.86% |
| AKE/USDT:USDT | below_1h_threshold | +2.43% | +2.48% |
| LONGXIA/USDT:USDT | below_1h_threshold | +1.84% | +1.89% |
| MARSCOIN/USDT:USDT | below_1h_threshold | +1.61% | +1.66% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
