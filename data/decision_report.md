# Decision Report

- generated_at: 2026-05-12T14:47:59.095091+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4131**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4131, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=-0.37%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.37% | **-0.37%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 8/20 | 40.0% | +0.95% | **+0.38%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_3PCT | 16/20 | 80.0% | -0.14% | **-0.12%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | -0.30% | **-0.14%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +1.57% | **+0.94%** |
| MARKET_LONG | 20/20 | 100.0% | +0.55% | **+0.55%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +0.76% | **+0.38%** |
| ASK_LONG | 20/20 | 100.0% | +0.38% | **+0.38%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +0.41% | **+0.31%** |

## 2. $100 Live Portfolio

- 残高: **$99.19** / 初期 $100.00 (-0.81%)
- 確定トレード: 34件 (TP 9 / SL 22 / EXP 3)
- 最新: DOGS/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.19
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$117.67** / 初期 $100.00 (+17.67%)
- 確定: 267件 (Win 74 / Loss 91 / Flat 102) / skip 425件
- 成長率目線: 平均log +0.000609 / 幾何平均 +0.061% per trade / maxDD +4.21%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: USELESS/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $117.67

## 4. Latest Market Context

- 更新: 2026-05-12T14:47:55.167629+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.23% price=80622.3
- Funnel: target 763 → liquid 197 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.9 >= 65=1, 4h RSI 85.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SAGA/USDT:USDT | +80.83% | $28,490,580.17 |
| GIGA/USDT:USDT | +65.97% | $7,585,531.97 |
| SKYAI/USDT:USDT | +41.28% | $40,300,345.79 |
| GUA/USDT:USDT | +35.31% | $3,753,251.08 |
| USELESS/USDT:USDT | +33.42% | $11,074,870.95 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PENGUIN/USDT:USDT | below_1h_threshold | +3.38% | +3.14% |
| B/USDT:USDT | below_1h_threshold | +2.01% | +1.78% |
| CYS/USDT:USDT | below_1h_threshold | +1.83% | +1.59% |
| NAORIS/USDT:USDT | below_1h_threshold | +1.64% | +1.41% |
| SAHARA/USDT:USDT | below_1h_threshold | +1.64% | +1.41% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
