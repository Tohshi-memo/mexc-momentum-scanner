# Decision Report

- generated_at: 2026-06-01T06:35:35.012956+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5281**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.35% / filled 20/20。**
- 全期間 MARKET基準: n=5281, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+1.35%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.35% | **+1.35%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.70% | **+1.70%** |
| MARKET | 20/20 | 100.0% | +1.35% | **+1.35%** |
| LIMIT_ATR | 15/20 | 75.0% | +1.70% | **+1.27%** |
| LIMIT_2PCT | 17/20 | 85.0% | +1.19% | **+1.02%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.60% | **+0.51%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +1.70% | **+0.94%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +0.39% | **+0.33%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +0.64% | **+0.32%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +0.70% | **+0.28%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +0.12% | **+0.08%** |

## 2. $100 Live Portfolio

- 残高: **$98.09** / 初期 $100.00 (-1.91%)
- 確定トレード: 81件 (TP 24 / SL 54 / EXP 3)
- 最新: GUN/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.09
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.03** / 初期 $100.00 (+31.03%)
- 確定: 894件 (Win 207 / Loss 269 / Flat 418) / skip 948件
- 成長率目線: 平均log +0.000302 / 幾何平均 +0.030% per trade / maxDD +7.25%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $131.03

## 4. Latest Market Context

- 更新: 2026-06-01T06:35:32.333946+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.22% price=73152.7
- Funnel: target 778 → liquid 136 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.9 >= 65=1, 4h RSI 87.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +156.41% | $31,512,934.23 |
| SLX/USDT:USDT | +145.39% | $2,227,066.10 |
| H/USDT:USDT | +67.70% | $24,169,517.24 |
| FHE/USDT:USDT | +28.40% | $1,270,673.45 |
| CTR/USDT:USDT | +25.41% | $1,601,694.62 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| XLM/USDT:USDT | below_1h_threshold | +4.02% | +4.24% |
| LAB/USDT:USDT | below_1h_threshold | +2.99% | +3.21% |
| BIANRENSHENG/USDT:USDT | below_1h_threshold | +2.66% | +2.89% |
| VVV/USDT:USDT | below_1h_threshold | +1.10% | +1.33% |
| SKYAI/USDT:USDT | below_1h_threshold | +0.94% | +1.16% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
