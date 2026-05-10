# Decision Report

- generated_at: 2026-05-10T07:27:58.562742+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3949**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.31% / filled 20/20。**
- 全期間 MARKET基準: n=3949, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+0.31%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.31% | **+0.31%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 6/20 | 30.0% | +1.67% | **+0.50%** |
| LIMIT_9PCT | 3/20 | 15.0% | +2.86% | **+0.43%** |
| ASK | 20/20 | 100.0% | +0.38% | **+0.38%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.39% | **+0.37%** |
| LIMIT_8PCT | 4/20 | 20.0% | +1.78% | **+0.36%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.68% | **+1.68%** |
| ASK_LONG | 20/20 | 100.0% | +1.31% | **+1.31%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.36% | **+1.09%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +1.47% | **+0.51%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +0.60% | **+0.18%** |

## 2. $100 Live Portfolio

- 残高: **$98.21** / 初期 $100.00 (-1.79%)
- 確定トレード: 30件 (TP 7 / SL 20 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.21
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$107.73** / 初期 $100.00 (+7.73%)
- 確定: 197件 (Win 48 / Loss 66 / Flat 83) / skip 313件
- 成長率目線: 平均log +0.000378 / 幾何平均 +0.038% per trade / maxDD +4.09%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LAYER/USDT:USDT `LIMIT_5PCT_LONG` EXPIRED account +0.00% 残高後 $107.73

## 4. Latest Market Context

- 更新: 2026-05-10T07:27:55.369197+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.07% price=80755.6
- Funnel: target 769 → liquid 165 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TROLLSOL/USDT:USDT | +62.64% | $1,240,860.66 |
| LAYER/USDT:USDT | +42.90% | $4,694,618.10 |
| XEC/USDT:USDT | +32.27% | $1,646,770.14 |
| BAS/USDT:USDT | +17.39% | $1,112,108.89 |
| SATO/USDT:USDT | +13.68% | $6,246,716.15 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| XEC/USDT:USDT | below_1h_threshold | +3.95% | +3.88% |
| INX/USDT:USDT | below_1h_threshold | +3.44% | +3.37% |
| LAYER/USDT:USDT | below_1h_threshold | +2.57% | +2.50% |
| FHE/USDT:USDT | below_1h_threshold | +1.75% | +1.69% |
| AIGENSYN/USDT:USDT | below_1h_threshold | +1.65% | +1.58% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
