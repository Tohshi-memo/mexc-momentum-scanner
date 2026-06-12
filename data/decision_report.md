# Decision Report

- generated_at: 2026-06-12T10:58:45.231085+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6503**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.95% / filled 20/20。**
- 全期間 MARKET基準: n=6503, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=+0.95%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.95% | **+0.95%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.96% | **+0.96%** |
| MARKET | 20/20 | 100.0% | +0.95% | **+0.95%** |
| LIMIT_BB3S | 7/18 | 38.9% | +2.35% | **+0.91%** |
| LIMIT_ATR | 12/20 | 60.0% | +1.14% | **+0.69%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.90% | **+0.67%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +4.87% | **+4.87%** |
| ASK_LONG | 20/20 | 100.0% | +0.66% | **+0.66%** |
| MARKET_LONG | 20/20 | 100.0% | +0.64% | **+0.64%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.22% | **+0.33%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.10% | **+0.16%** |

## 2. $100 Live Portfolio

- 残高: **$94.70** / 初期 $100.00 (-5.30%)
- 確定トレード: 18件 (TP 2 / SL 15 / EXP 1)
- 最新: MYX/USDT:USDT SL_HIT PnL -3.58% 残高後 $94.70
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$168.05** / 初期 $100.00 (+68.05%)
- 確定: 1376件 (Win 377 / Loss 443 / Flat 556) / skip 1688件
- 成長率目線: 平均log +0.000377 / 幾何平均 +0.038% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MYX/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $168.05

## 4. Latest Market Context

- 更新: 2026-06-12T10:58:41.888861+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.08% price=63674.6
- Funnel: target 774 → liquid 159 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 75.8 >= 65=1, 4h RSI 73.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +92.69% | $156,024,159.81 |
| ESPORTS/USDT:USDT | +71.81% | $44,658,578.16 |
| NAORIS/USDT:USDT | +44.50% | $4,886,079.82 |
| XPL/USDT:USDT | +39.50% | $11,903,400.93 |
| AIN/USDT:USDT | +33.59% | $1,104,010.01 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TRUMPOFFICIAL/USDT:USDT | below_1h_threshold | +3.79% | +3.87% |
| AIN/USDT:USDT | below_1h_threshold | +2.75% | +2.83% |
| ZRO/USDT:USDT | below_1h_threshold | +2.53% | +2.61% |
| WLFI/USDT:USDT | below_1h_threshold | +2.10% | +2.19% |
| SEI/USDT:USDT | below_1h_threshold | +1.39% | +1.48% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
