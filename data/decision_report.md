# Decision Report

- generated_at: 2026-06-15T03:39:52.108851+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6730**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.32% / filled 20/20。**
- 全期間 MARKET基準: n=6730, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+1.32%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.32% | **+1.32%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 18/20 | 90.0% | +2.25% | **+2.02%** |
| ASK | 20/20 | 100.0% | +1.68% | **+1.68%** |
| MARKET | 20/20 | 100.0% | +1.32% | **+1.32%** |
| LIMIT_2PCT | 16/20 | 80.0% | +1.53% | **+1.23%** |
| LIMIT_3PCT | 13/20 | 65.0% | +1.18% | **+0.77%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +3.64% | **+1.09%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +2.22% | **+1.00%** |
| LIMIT_9PCT_LONG | 7/20 | 35.0% | +2.34% | **+0.82%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +0.15% | **+0.08%** |

## 2. $100 Live Portfolio

- 残高: **$100.99** / 初期 $100.00 (+0.99%)
- 確定トレード: 4件 (TP 2 / SL 2 / EXP 0)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.99
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$174.41** / 初期 $100.00 (+74.41%)
- 確定: 1603件 (Win 423 / Loss 500 / Flat 680) / skip 1688件
- 成長率目線: 平均log +0.000347 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ASTEROID/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $174.41

## 4. Robust Adaptive DryRun ($100)

- 残高: **$99.86** / 初期 $100.00 (-0.14%)
- 確定: 98件 (Win 23 / Loss 16 / Flat 59) / skip 43件
- 成長率目線: 平均log -0.000014 / 幾何平均 -0.001% per trade / maxDD +2.07%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0605 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ASTEROID/USDT:USDT `LIMIT_9PCT_LONG` TP_HIT account +0.69% 残高後 $99.86

## 5. Latest Market Context

- 更新: 2026-06-15T03:39:46.113810+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.37% price=65676.2
- Funnel: target 770 → liquid 142 → pre 50 → checked 50 → surge 5 → strict 1
- Surge前reject: below_1h_threshold=45, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.1 >= 65=1, 4h RSI 92.3 >= 65=1, 4h RSI 74.9 >= 65=1, 4h RSI 75.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ASTEROID/USDT:USDT | +131.64% | $1,544,287.10 |
| EVAA/USDT:USDT | +52.40% | $18,096,763.04 |
| CLO/USDT:USDT | +32.79% | $2,045,000.51 |
| RIF/USDT:USDT | +32.33% | $4,646,219.83 |
| GRASS/USDT:USDT | +21.59% | $1,001,836.65 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GRASS/USDT:USDT | below_1h_threshold | +2.46% | +2.08% |
| CHIP/USDT:USDT | below_1h_threshold | +1.75% | +1.38% |
| OPG/USDT:USDT | below_1h_threshold | +1.58% | +1.21% |
| ONDO/USDT:USDT | below_1h_threshold | +1.44% | +1.07% |
| JTO/USDT:USDT | below_1h_threshold | +1.12% | +0.74% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
