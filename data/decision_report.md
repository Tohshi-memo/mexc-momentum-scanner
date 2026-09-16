# Decision Report

- generated_at: 2026-09-16T10:26:24.444031+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14662**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14662, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.44%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.44% | **-0.44%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 11/20 | 55.0% | +0.88% | **+0.49%** |
| LIMIT_BB3S | 6/13 | 46.2% | +0.84% | **+0.39%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.31% | **+0.20%** |
| LIMIT_7PCT | 6/20 | 30.0% | +0.27% | **+0.08%** |
| LIMIT_ATR | 15/20 | 75.0% | +0.05% | **+0.04%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.65% | **+1.40%** |
| LIMIT_BB3S_LONG | 4/7 | 57.1% | +2.27% | **+1.30%** |
| MARKET_LONG | 20/20 | 100.0% | +0.99% | **+0.99%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +2.41% | **+0.60%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.00% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 214件 (TP 79 / SL 130 / EXP 5)
- 最新: SHROOM/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,034.96** / 初期 $100.00 (+934.96%)
- 確定: 5540件 (Win 1649 / Loss 1791 / Flat 2100) / skip 5683件
- 成長率目線: 平均log +0.000422 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BR/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $1,034.96

## 4. Robust Adaptive DryRun ($100)

- 残高: **$228.85** / 初期 $100.00 (+128.85%)
- 確定: 3068件 (Win 842 / Loss 722 / Flat 1504) / skip 5005件
- 成長率目線: 平均log +0.000270 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0123 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BR/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $228.85

## 5. Causal Adaptive DryRun ($100)

- 残高: **$124.62** / 初期 $100.00 (+24.62%)
- 確定: 2951件 (Win 878 / Loss 1160 / Flat 913) / pending 2件 / skip 3179件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000246 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BR/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $124.62

## 6. Latest Market Context

- 更新: 2026-09-16T10:26:09.677213+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.08% price=75895.5
- Funnel: target 1058 → liquid 154 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SYN/USDT:USDT | +112.37% | $16,495,357.64 |
| LSK/USDT:USDT | +32.02% | $21,485,492.81 |
| BR/USDT:USDT | +30.34% | $16,403,412.11 |
| USELESS/USDT:USDT | +15.18% | $7,378,399.20 |
| MARSCOIN/USDT:USDT | +11.55% | $1,745,103.78 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CNPY/USDT:USDT | below_1h_threshold | +3.72% | +3.81% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.56% | +2.64% |
| MARSCOIN/USDT:USDT | below_1h_threshold | +1.56% | +1.64% |
| 4/USDT:USDT | below_1h_threshold | +1.11% | +1.19% |
| AKE/USDT:USDT | below_1h_threshold | +0.57% | +0.66% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
