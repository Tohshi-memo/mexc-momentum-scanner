# Decision Report

- generated_at: 2026-06-15T03:33:12.956866+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6729**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.32% / filled 20/20。**
- 全期間 MARKET基準: n=6729, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+1.32%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.32% | **+1.32%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 18/20 | 90.0% | +1.58% | **+1.42%** |
| MARKET | 20/20 | 100.0% | +1.32% | **+1.32%** |
| ASK | 20/20 | 100.0% | +1.08% | **+1.08%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.91% | **+0.73%** |
| LIMIT_3PCT | 13/20 | 65.0% | +0.49% | **+0.32%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +3.64% | **+1.09%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.50% | **+0.60%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +1.40% | **+0.42%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.62% | **+0.28%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | -0.50% | **-0.23%** |

## 2. $100 Live Portfolio

- 残高: **$100.99** / 初期 $100.00 (+0.99%)
- 確定トレード: 4件 (TP 2 / SL 2 / EXP 0)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.99
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$174.41** / 初期 $100.00 (+74.41%)
- 確定: 1602件 (Win 423 / Loss 500 / Flat 679) / skip 1688件
- 成長率目線: 平均log +0.000347 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ASTEROID/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $174.41

## 4. Robust Adaptive DryRun ($100)

- 残高: **$99.18** / 初期 $100.00 (-0.82%)
- 確定: 97件 (Win 22 / Loss 16 / Flat 59) / skip 43件
- 成長率目線: 平均log -0.000085 / 幾何平均 -0.008% per trade / maxDD +2.07%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0438 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ASTEROID/USDT:USDT `LIMIT_9PCT_LONG` SL_HIT account -0.35% 残高後 $99.18

## 5. Latest Market Context

- 更新: 2026-06-15T03:33:07.888645+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.40% price=65694.1
- Funnel: target 770 → liquid 141 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 74.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ASTEROID/USDT:USDT | +143.00% | $1,364,607.56 |
| EVAA/USDT:USDT | +43.66% | $17,946,649.20 |
| CLO/USDT:USDT | +32.85% | $2,033,965.17 |
| RIF/USDT:USDT | +30.62% | $4,632,734.28 |
| USELESS/USDT:USDT | +17.61% | $1,214,242.34 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| H/USDT:USDT | below_relative_strength | +5.03% | +4.62% |
| RIF/USDT:USDT | below_1h_threshold | +4.72% | +4.32% |
| CHIP/USDT:USDT | below_1h_threshold | +3.30% | +2.89% |
| EVAA/USDT:USDT | below_1h_threshold | +2.31% | +1.90% |
| USELESS/USDT:USDT | below_1h_threshold | +1.67% | +1.27% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
