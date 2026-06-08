# Decision Report

- generated_at: 2026-06-08T01:50:17.734582+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6019**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6019, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=-1.57%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.57% | **-1.57%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 10/20 | 50.0% | +0.95% | **+0.48%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.32% | **+0.46%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_BB3S | 2/16 | 12.5% | +1.81% | **+0.23%** |
| LIMIT_4PCT | 16/20 | 80.0% | +0.03% | **+0.03%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.42% | **+1.35%** |
| ASK_LONG | 20/20 | 100.0% | +0.99% | **+0.99%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +2.33% | **+0.93%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +2.97% | **+0.89%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.14% | **+0.85%** |

## 2. $100 Live Portfolio

- 残高: **$99.07** / 初期 $100.00 (-0.93%)
- 確定トレード: 6件 (TP 1 / SL 4 / EXP 1)
- 最新: LUNC/USDT:USDT EXPIRED PnL +0.53% 残高後 $99.07
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$154.45** / 初期 $100.00 (+54.45%)
- 確定: 1136件 (Win 278 / Loss 344 / Flat 514) / skip 1444件
- 成長率目線: 平均log +0.000383 / 幾何平均 +0.038% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BLESS/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $154.45

## 4. Latest Market Context

- 更新: 2026-06-08T01:50:10.860377+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.87% price=63044.2
- Funnel: target 773 → liquid 142 → pre 50 → checked 50 → surge 4 → strict 1
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 68.6 >= 65=1, 4h RSI 83.2 >= 65=1, 4h RSI 88.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BEAT/USDT:USDT | +34.81% | $90,214,780.84 |
| BANK/USDT:USDT | +33.81% | $4,641,508.30 |
| BLESS/USDT:USDT | +29.98% | $8,313,752.01 |
| EPIC/USDT:USDT | +24.21% | $1,572,432.20 |
| ESPORTS/USDT:USDT | +24.20% | $5,492,780.79 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BANK/USDT:USDT | below_1h_threshold | +4.62% | +5.49% |
| BEAT/USDT:USDT | below_1h_threshold | +4.32% | +5.20% |
| OPENAI/USDT:USDT | below_1h_threshold | +2.11% | +2.98% |
| MYX/USDT:USDT | below_1h_threshold | +1.75% | +2.62% |
| USOIL/USDT:USDT | below_1h_threshold | +0.99% | +1.86% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
