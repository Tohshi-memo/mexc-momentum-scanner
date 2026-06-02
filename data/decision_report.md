# Decision Report

- generated_at: 2026-06-02T11:00:09.633927+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5444**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=5444, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.88% | **+0.88%** |
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_4PCT | 12/20 | 60.0% | +1.00% | **+0.60%** |
| LIMIT_5PCT | 5/20 | 25.0% | +1.37% | **+0.34%** |
| LIMIT_BB3S | 5/15 | 33.3% | +0.09% | **+0.03%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +0.89% | **+0.22%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +0.55% | **+0.16%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | -0.50% | **-0.08%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | -0.12% | **-0.08%** |
| ASK_LONG | 20/20 | 100.0% | -0.18% | **-0.18%** |

## 2. $100 Live Portfolio

- 残高: **$97.10** / 初期 $100.00 (-2.90%)
- 確定トレード: 86件 (TP 25 / SL 58 / EXP 3)
- 最新: LIT/USDT:USDT TP_HIT PnL +8.00% 残高後 $97.10
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$132.63** / 初期 $100.00 (+32.63%)
- 確定: 956件 (Win 224 / Loss 289 / Flat 443) / skip 1049件
- 成長率目線: 平均log +0.000295 / 幾何平均 +0.030% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PIEVERSE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $132.63

## 4. Latest Market Context

- 更新: 2026-06-02T11:00:06.080722+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.34% price=69631.0
- Funnel: target 772 → liquid 155 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 70.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| US/USDT:USDT | +43.47% | $3,045,927.93 |
| EPIC/USDT:USDT | +29.19% | $2,476,889.93 |
| MRVLSTOCK/USDT:USDT | +26.72% | $5,478,863.08 |
| ESPORTS/USDT:USDT | +25.71% | $12,972,110.44 |
| UB/USDT:USDT | +24.02% | $3,179,030.97 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| USELESS/USDT:USDT | below_1h_threshold | +4.60% | +4.26% |
| UB/USDT:USDT | below_1h_threshold | +4.23% | +3.89% |
| SLX/USDT:USDT | below_1h_threshold | +4.15% | +3.81% |
| EPIC/USDT:USDT | below_1h_threshold | +4.10% | +3.75% |
| PIEVERSE/USDT:USDT | below_1h_threshold | +3.86% | +3.52% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
