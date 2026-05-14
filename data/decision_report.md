# Decision Report

- generated_at: 2026-05-14T07:29:31.652958+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4276**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.93% / filled 20/20。**
- 全期間 MARKET基準: n=4276, expectancy=-0.11%
- 直近20件 MARKET基準: n=20, expectancy=+0.93%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.93% | **+0.93%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 15/20 | 75.0% | +1.44% | **+1.08%** |
| LIMIT_2PCT | 17/20 | 85.0% | +1.21% | **+1.03%** |
| LIMIT_BB3S | 4/16 | 25.0% | +4.06% | **+1.02%** |
| ASK | 20/20 | 100.0% | +0.98% | **+0.98%** |
| MARKET | 20/20 | 100.0% | +0.93% | **+0.93%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +4.07% | **+4.07%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +2.16% | **+0.86%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.69% | **+0.67%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |
| MARKET_LONG | 20/20 | 100.0% | +0.39% | **+0.39%** |

## 2. $100 Live Portfolio

- 残高: **$97.21** / 初期 $100.00 (-2.79%)
- 確定トレード: 41件 (TP 10 / SL 28 / EXP 3)
- 最新: SAGA/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.21
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$119.18** / 初期 $100.00 (+19.18%)
- 確定: 344件 (Win 94 / Loss 125 / Flat 125) / skip 493件
- 成長率目線: 平均log +0.000510 / 幾何平均 +0.051% per trade / maxDD +4.21%
- 次の候補: `LIMIT_7PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GIGA/USDT:USDT `LIMIT_7PCT_LONG` EXPIRED account +0.00% 残高後 $119.18

## 4. Latest Market Context

- 更新: 2026-05-14T07:29:28.249863+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=79794.2
- Funnel: target 766 → liquid 169 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TROLLSOL/USDT:USDT | +33.98% | $2,047,516.22 |
| STAR/USDT:USDT | +22.56% | $1,201,759.97 |
| CSCOSTOCK/USDT:USDT | +21.46% | $5,163,671.07 |
| GIGA/USDT:USDT | +19.84% | $1,160,087.97 |
| UP/USDT:USDT | +18.67% | $5,299,984.19 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| Q/USDT:USDT | below_1h_threshold | +3.61% | +3.58% |
| KITE/USDT:USDT | below_1h_threshold | +2.01% | +1.97% |
| AIGENSYN/USDT:USDT | below_1h_threshold | +1.61% | +1.58% |
| CSCOSTOCK/USDT:USDT | below_1h_threshold | +1.42% | +1.39% |
| PIEVERSE/USDT:USDT | below_1h_threshold | +0.97% | +0.94% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
