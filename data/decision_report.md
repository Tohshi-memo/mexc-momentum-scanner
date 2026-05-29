# Decision Report

- generated_at: 2026-05-29T00:39:41.052603+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4998**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.47% / filled 20/20。**
- 全期間 MARKET基準: n=4998, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=+0.47%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.47% | **+0.47%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| ASK | 20/20 | 100.0% | +0.54% | **+0.54%** |
| MARKET | 20/20 | 100.0% | +0.47% | **+0.47%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.27% | **+0.34%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.96% | **+0.29%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +2.45% | **+0.98%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +1.72% | **+0.86%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +1.69% | **+0.34%** |
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +0.29% | **+0.29%** |

## 2. $100 Live Portfolio

- 残高: **$98.61** / 初期 $100.00 (-1.39%)
- 確定トレード: 71件 (TP 21 / SL 47 / EXP 3)
- 最新: BILL/USDT:USDT TP_HIT PnL +8.00% 残高後 $98.61
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$128.23** / 初期 $100.00 (+28.23%)
- 確定: 729件 (Win 175 / Loss 222 / Flat 332) / skip 830件
- 成長率目線: 平均log +0.000341 / 幾何平均 +0.034% per trade / maxDD +4.72%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SKYAI/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $128.23

## 4. Latest Market Context

- 更新: 2026-05-29T00:39:38.192649+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.30% price=73810.9
- Funnel: target 774 → liquid 159 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 78.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ALLO/USDT:USDT | +51.49% | $20,931,502.64 |
| DELLSTOCK/USDT:USDT | +31.44% | $7,071,670.21 |
| CLO/USDT:USDT | +21.42% | $1,217,492.91 |
| ALGO/USDT:USDT | +14.01% | $3,399,279.75 |
| BSB/USDT:USDT | +12.52% | $13,535,915.50 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BSB/USDT:USDT | below_1h_threshold | +4.03% | +3.73% |
| AR/USDT:USDT | below_1h_threshold | +3.33% | +3.03% |
| FIDA/USDT:USDT | below_1h_threshold | +2.96% | +2.67% |
| ALGO/USDT:USDT | below_1h_threshold | +2.86% | +2.56% |
| BAT/USDT:USDT | below_1h_threshold | +2.70% | +2.40% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
