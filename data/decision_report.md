# Decision Report

- generated_at: 2026-06-01T06:45:49.841632+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5283**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.55% / filled 20/20。**
- 全期間 MARKET基準: n=5283, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+2.55%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.55% | **+2.55%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +2.82% | **+2.82%** |
| MARKET | 20/20 | 100.0% | +2.55% | **+2.55%** |
| LIMIT_2PCT | 17/20 | 85.0% | +2.37% | **+2.01%** |
| LIMIT_ATR | 14/20 | 70.0% | +2.41% | **+1.68%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.95% | **+1.66%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +0.23% | **+0.14%** |
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +0.15% | **+0.13%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +0.77% | **+0.12%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +0.18% | **+0.08%** |
| LIMIT_9PCT_LONG | 7/20 | 35.0% | -0.36% | **-0.13%** |

## 2. $100 Live Portfolio

- 残高: **$98.09** / 初期 $100.00 (-1.91%)
- 確定トレード: 81件 (TP 24 / SL 54 / EXP 3)
- 最新: GUN/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.09
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.03** / 初期 $100.00 (+31.03%)
- 確定: 894件 (Win 207 / Loss 269 / Flat 418) / skip 950件
- 成長率目線: 平均log +0.000302 / 幾何平均 +0.030% per trade / maxDD +7.25%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $131.03

## 4. Latest Market Context

- 更新: 2026-06-01T06:45:46.809248+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.50% price=72950.1
- Funnel: target 778 → liquid 137 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.7 >= 65=1, 4h RSI 87.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +151.08% | $31,815,286.80 |
| SLX/USDT:USDT | +129.79% | $2,599,233.22 |
| H/USDT:USDT | +72.05% | $24,529,703.06 |
| CTR/USDT:USDT | +26.24% | $1,608,552.57 |
| LAB/USDT:USDT | +24.08% | $193,464,188.57 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +4.73% | +5.23% |
| XLM/USDT:USDT | below_1h_threshold | +3.81% | +4.31% |
| SIREN/USDT:USDT | below_1h_threshold | +1.54% | +2.04% |
| BIANRENSHENG/USDT:USDT | below_1h_threshold | +1.22% | +1.72% |
| GUA/USDT:USDT | below_1h_threshold | +1.19% | +1.69% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
