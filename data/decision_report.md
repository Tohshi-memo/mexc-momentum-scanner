# Decision Report

- generated_at: 2026-06-15T03:52:49.016723+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6734**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.97% / filled 20/20。**
- 全期間 MARKET基準: n=6734, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+0.97%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.97% | **+0.97%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.59% | **+1.59%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.75% | **+1.58%** |
| MARKET | 20/20 | 100.0% | +0.97% | **+0.97%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.85% | **+0.68%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.25% | **+0.44%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +3.70% | **+1.11%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +1.78% | **+0.80%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_FIB1272_LONG | 5/20 | 25.0% | +1.89% | **+0.47%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | -0.14% | **-0.07%** |

## 2. $100 Live Portfolio

- 残高: **$100.99** / 初期 $100.00 (+0.99%)
- 確定トレード: 4件 (TP 2 / SL 2 / EXP 0)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.99
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$173.89** / 初期 $100.00 (+73.89%)
- 確定: 1607件 (Win 423 / Loss 501 / Flat 683) / skip 1688件
- 成長率目線: 平均log +0.000344 / 幾何平均 +0.034% per trade / maxDD +7.25%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ASTEROID/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $173.89

## 4. Robust Adaptive DryRun ($100)

- 残高: **$100.55** / 初期 $100.00 (+0.55%)
- 確定: 101件 (Win 24 / Loss 16 / Flat 61) / skip 44件
- 成長率目線: 平均log +0.000054 / 幾何平均 +0.005% per trade / maxDD +2.07%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0744 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ASTEROID/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $100.55

## 5. Latest Market Context

- 更新: 2026-06-15T03:52:42.359583+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.67% price=65867.5
- Funnel: target 770 → liquid 142 → pre 50 → checked 50 → surge 4 → strict 1
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 71.9 >= 65=1, 4h RSI 92.8 >= 65=1, 4h RSI 75.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ASTEROID/USDT:USDT | +139.16% | $1,767,278.73 |
| EVAA/USDT:USDT | +58.29% | $18,395,840.15 |
| CLO/USDT:USDT | +35.74% | $2,068,936.44 |
| RIF/USDT:USDT | +35.65% | $4,702,814.82 |
| GRASS/USDT:USDT | +22.69% | $1,053,936.18 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GRASS/USDT:USDT | below_1h_threshold | +3.40% | +2.73% |
| ONDO/USDT:USDT | below_1h_threshold | +1.76% | +1.10% |
| USELESS/USDT:USDT | below_1h_threshold | +1.46% | +0.79% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.44% | +0.77% |
| CHIP/USDT:USDT | below_1h_threshold | +1.39% | +0.72% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
