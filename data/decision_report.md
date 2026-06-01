# Decision Report

- generated_at: 2026-06-01T10:53:38.009665+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5308**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.77% / filled 20/20。**
- 全期間 MARKET基準: n=5308, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.77%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.77% | **+0.77%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 18/20 | 90.0% | +1.89% | **+1.70%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.82% | **+0.78%** |
| MARKET | 20/20 | 100.0% | +0.77% | **+0.77%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +3.53% | **+0.71%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.73% | **+0.55%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +1.30% | **+0.59%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.60% | **+0.54%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.57% | **+0.20%** |
| MARKET_LONG | 20/20 | 100.0% | +0.12% | **+0.12%** |
| ASK_LONG | 20/20 | 100.0% | +0.05% | **+0.05%** |

## 2. $100 Live Portfolio

- 残高: **$97.60** / 初期 $100.00 (-2.40%)
- 確定トレード: 82件 (TP 24 / SL 55 / EXP 3)
- 最新: GUA/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.60
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.03** / 初期 $100.00 (+31.03%)
- 確定: 894件 (Win 207 / Loss 269 / Flat 418) / skip 975件
- 成長率目線: 平均log +0.000302 / 幾何平均 +0.030% per trade / maxDD +7.25%
- 次の候補: `LIMIT_5PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $131.03

## 4. Latest Market Context

- 更新: 2026-06-01T10:53:32.502510+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.14% price=72752.8
- Funnel: target 776 → liquid 133 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 87.3 >= 65=1, 4h RSI 89.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +142.75% | $36,247,399.40 |
| SLX/USDT:USDT | +106.46% | $7,203,524.90 |
| H/USDT:USDT | +93.05% | $32,479,362.95 |
| LAB/USDT:USDT | +81.50% | $225,691,391.80 |
| VIC/USDT:USDT | +66.06% | $1,004,081.67 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PORTAL/USDT:USDT | below_1h_threshold | +3.81% | +3.94% |
| XLM/USDT:USDT | below_1h_threshold | +3.69% | +3.83% |
| SLX/USDT:USDT | below_1h_threshold | +3.37% | +3.51% |
| XMR/USDT:USDT | below_1h_threshold | +2.33% | +2.47% |
| FET/USDT:USDT | below_1h_threshold | +1.79% | +1.92% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
