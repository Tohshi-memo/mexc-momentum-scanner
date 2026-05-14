# Decision Report

- generated_at: 2026-05-14T09:58:01.044219+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4278**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.69% / filled 20/20。**
- 全期間 MARKET基準: n=4278, expectancy=-0.11%
- 直近20件 MARKET基準: n=20, expectancy=+0.69%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.69% | **+0.69%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 4/16 | 25.0% | +4.06% | **+1.02%** |
| ASK | 20/20 | 100.0% | +0.74% | **+0.74%** |
| MARKET | 20/20 | 100.0% | +0.69% | **+0.69%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.78% | **+0.63%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.87% | **+0.61%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +4.07% | **+4.07%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +2.77% | **+0.97%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +2.08% | **+0.73%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +1.33% | **+0.40%** |
| MARKET_LONG | 20/20 | 100.0% | +0.39% | **+0.39%** |

## 2. $100 Live Portfolio

- 残高: **$97.21** / 初期 $100.00 (-2.79%)
- 確定トレード: 41件 (TP 10 / SL 28 / EXP 3)
- 最新: SAGA/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.21
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$119.18** / 初期 $100.00 (+19.18%)
- 確定: 344件 (Win 94 / Loss 125 / Flat 125) / skip 495件
- 成長率目線: 平均log +0.000510 / 幾何平均 +0.051% per trade / maxDD +4.21%
- 次の候補: `LIMIT_7PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GIGA/USDT:USDT `LIMIT_7PCT_LONG` EXPIRED account +0.00% 残高後 $119.18

## 4. Latest Market Context

- 更新: 2026-05-14T09:57:57.506222+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.27% price=79564.7
- Funnel: target 763 → liquid 164 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TROLLSOL/USDT:USDT | +27.49% | $2,173,043.94 |
| UP/USDT:USDT | +23.75% | $5,406,310.58 |
| STAR/USDT:USDT | +20.39% | $1,852,047.53 |
| CSCOSTOCK/USDT:USDT | +19.37% | $5,323,765.89 |
| PIEVERSE/USDT:USDT | +18.94% | $2,282,610.04 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| H/USDT:USDT | below_1h_threshold | +3.13% | +3.39% |
| TRIA/USDT:USDT | below_1h_threshold | +2.33% | +2.60% |
| GUA/USDT:USDT | below_1h_threshold | +2.32% | +2.58% |
| XPL/USDT:USDT | below_1h_threshold | +1.17% | +1.44% |
| JTO/USDT:USDT | below_1h_threshold | +1.07% | +1.34% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
