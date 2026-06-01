# Decision Report

- generated_at: 2026-06-01T10:47:56.484637+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5307**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.77% / filled 20/20。**
- 全期間 MARKET基準: n=5307, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.77%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.77% | **+0.77%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 18/20 | 90.0% | +1.78% | **+1.60%** |
| LIMIT_FIB1272 | 3/20 | 15.0% | +5.23% | **+0.78%** |
| MARKET | 20/20 | 100.0% | +0.77% | **+0.77%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.77% | **+0.73%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.73% | **+0.55%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +1.30% | **+0.59%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.60% | **+0.54%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.57% | **+0.20%** |
| MARKET_LONG | 20/20 | 100.0% | +0.12% | **+0.12%** |
| ASK_LONG | 20/20 | 100.0% | +0.10% | **+0.10%** |

## 2. $100 Live Portfolio

- 残高: **$97.60** / 初期 $100.00 (-2.40%)
- 確定トレード: 82件 (TP 24 / SL 55 / EXP 3)
- 最新: GUA/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.60
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.03** / 初期 $100.00 (+31.03%)
- 確定: 894件 (Win 207 / Loss 269 / Flat 418) / skip 974件
- 成長率目線: 平均log +0.000302 / 幾何平均 +0.030% per trade / maxDD +7.25%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $131.03

## 4. Latest Market Context

- 更新: 2026-06-01T10:47:52.999112+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.20% price=72705.6
- Funnel: target 776 → liquid 132 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 88.3 >= 65=1, 4h RSI 89.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +136.92% | $36,138,865.55 |
| SLX/USDT:USDT | +99.23% | $7,044,726.96 |
| H/USDT:USDT | +96.46% | $32,273,707.16 |
| LAB/USDT:USDT | +91.41% | $223,525,977.44 |
| WLD/USDT:USDT | +18.03% | $85,162,323.33 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HEI/USDT:USDT | below_1h_threshold | +4.18% | +4.38% |
| XLM/USDT:USDT | below_1h_threshold | +2.94% | +3.14% |
| BILL/USDT:USDT | below_1h_threshold | +2.63% | +2.83% |
| FET/USDT:USDT | below_1h_threshold | +2.61% | +2.81% |
| XMR/USDT:USDT | below_1h_threshold | +2.10% | +2.30% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
