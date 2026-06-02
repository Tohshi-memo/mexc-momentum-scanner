# Decision Report

- generated_at: 2026-06-02T12:18:51.767686+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5451**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.40% / filled 20/20。**
- 全期間 MARKET基準: n=5451, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+1.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.40% | **+1.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.42% | **+1.42%** |
| MARKET | 20/20 | 100.0% | +1.40% | **+1.40%** |
| LIMIT_4PCT | 11/20 | 55.0% | +1.09% | **+0.60%** |
| LIMIT_BB3S | 5/15 | 33.3% | +1.75% | **+0.58%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.66% | **+0.56%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 6/20 | 30.0% | +0.07% | **+0.02%** |
| LIMIT_9PCT_LONG | 7/20 | 35.0% | -0.10% | **-0.04%** |
| ASK_LONG | 20/20 | 100.0% | -0.09% | **-0.09%** |
| LIMIT_7PCT_LONG | 11/20 | 55.0% | -0.49% | **-0.27%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | -1.38% | **-0.28%** |

## 2. $100 Live Portfolio

- 残高: **$96.62** / 初期 $100.00 (-3.38%)
- 確定トレード: 87件 (TP 25 / SL 59 / EXP 3)
- 最新: SLX/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.62
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$132.66** / 初期 $100.00 (+32.66%)
- 確定: 963件 (Win 226 / Loss 292 / Flat 445) / skip 1049件
- 成長率目線: 平均log +0.000293 / 幾何平均 +0.029% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EPIC/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $132.66

## 4. Latest Market Context

- 更新: 2026-06-02T12:18:49.230335+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.27% price=69241.4
- Funnel: target 773 → liquid 150 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 71.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| US/USDT:USDT | +31.84% | $3,604,095.86 |
| EPIC/USDT:USDT | +29.61% | $2,923,389.39 |
| USELESS/USDT:USDT | +25.74% | $2,610,152.80 |
| CLO/USDT:USDT | +24.49% | $1,072,813.79 |
| LAB/USDT:USDT | +23.97% | $171,577,124.05 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BILL/USDT:USDT | below_1h_threshold | +2.46% | +2.74% |
| OPG/USDT:USDT | below_1h_threshold | +2.45% | +2.72% |
| UB/USDT:USDT | below_1h_threshold | +2.38% | +2.65% |
| SLX/USDT:USDT | below_1h_threshold | +1.57% | +1.84% |
| RIF/USDT:USDT | below_1h_threshold | +1.49% | +1.76% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
