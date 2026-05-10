# Decision Report

- generated_at: 2026-05-10T07:47:38.601992+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3951**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.48% / filled 20/20。**
- 全期間 MARKET基準: n=3951, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+0.48%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.48% | **+0.48%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 6/20 | 30.0% | +1.67% | **+0.50%** |
| ASK | 20/20 | 100.0% | +0.49% | **+0.49%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.51% | **+0.48%** |
| MARKET | 20/20 | 100.0% | +0.48% | **+0.48%** |
| LIMIT_9PCT | 3/20 | 15.0% | +2.86% | **+0.43%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.62% | **+1.62%** |
| ASK_LONG | 20/20 | 100.0% | +1.29% | **+1.29%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.29% | **+1.03%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +1.48% | **+0.44%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +1.02% | **+0.41%** |

## 2. $100 Live Portfolio

- 残高: **$98.21** / 初期 $100.00 (-1.79%)
- 確定トレード: 30件 (TP 7 / SL 20 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.21
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$107.73** / 初期 $100.00 (+7.73%)
- 確定: 197件 (Win 48 / Loss 66 / Flat 83) / skip 315件
- 成長率目線: 平均log +0.000378 / 幾何平均 +0.038% per trade / maxDD +4.09%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LAYER/USDT:USDT `LIMIT_5PCT_LONG` EXPIRED account +0.00% 残高後 $107.73

## 4. Latest Market Context

- 更新: 2026-05-10T07:47:34.841026+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.07% price=80754.9
- Funnel: target 769 → liquid 166 → pre 50 → checked 50 → surge 4 → strict 0
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.5 >= 65=1, 4h RSI 69.9 >= 65=1, 4h RSI 93.1 >= 65=1, 4h RSI 79.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TROLLSOL/USDT:USDT | +65.04% | $1,304,102.18 |
| LAYER/USDT:USDT | +48.37% | $5,045,345.96 |
| XEC/USDT:USDT | +31.21% | $1,755,141.16 |
| BAS/USDT:USDT | +17.10% | $1,135,344.24 |
| LAB/USDT:USDT | +16.73% | $101,589,166.53 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SATO/USDT:USDT | below_1h_threshold | +3.18% | +3.11% |
| XEC/USDT:USDT | below_1h_threshold | +3.12% | +3.05% |
| AIGENSYN/USDT:USDT | below_1h_threshold | +1.94% | +1.88% |
| ENS/USDT:USDT | below_1h_threshold | +1.86% | +1.79% |
| PYTH/USDT:USDT | below_1h_threshold | +1.67% | +1.60% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
