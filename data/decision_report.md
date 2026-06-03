# Decision Report

- generated_at: 2026-06-03T10:58:18.687975+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5540**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5540, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.24%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.24% | **-1.24%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 6/20 | 30.0% | +2.13% | **+0.64%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.78% | **+0.62%** |
| LIMIT_ATR | 18/20 | 90.0% | +0.57% | **+0.52%** |
| LIMIT_3PCT | 17/20 | 85.0% | +0.44% | **+0.37%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +1.27% | **+1.27%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +1.61% | **+0.80%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.96% | **+0.67%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.05% | **+0.63%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +1.02% | **+0.46%** |

## 2. $100 Live Portfolio

- 残高: **$96.61** / 初期 $100.00 (-3.39%)
- 確定トレード: 90件 (TP 26 / SL 61 / EXP 3)
- 最新: VVV/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.61
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$133.02** / 初期 $100.00 (+33.02%)
- 確定: 994件 (Win 237 / Loss 306 / Flat 451) / skip 1107件
- 成長率目線: 平均log +0.000287 / 幾何平均 +0.029% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EPIC/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +1.00% 残高後 $133.02

## 4. Latest Market Context

- 更新: 2026-06-03T10:58:12.979705+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.32% price=67252.3
- Funnel: target 771 → liquid 153 → pre 50 → checked 50 → surge 5 → strict 1
- Surge前reject: below_1h_threshold=45, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.7 >= 65=1, 4h RSI 72.9 >= 65=1, 4h RSI 91.5 >= 65=1, 4h RSI 71.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CLO/USDT:USDT | +44.21% | $4,416,291.92 |
| EPIC/USDT:USDT | +43.23% | $2,954,679.01 |
| ENA/USDT:USDT | +29.34% | $56,877,002.43 |
| APR/USDT:USDT | +28.77% | $1,454,078.09 |
| LIT/USDT:USDT | +27.44% | $9,002,117.37 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NEAR/USDT:USDT | below_1h_threshold | +4.77% | +4.46% |
| OP/USDT:USDT | below_1h_threshold | +4.50% | +4.19% |
| VIRTUAL/USDT:USDT | below_1h_threshold | +4.06% | +3.74% |
| DYDX/USDT:USDT | below_1h_threshold | +3.96% | +3.65% |
| MRVLSTOCK/USDT:USDT | below_1h_threshold | +3.76% | +3.44% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
