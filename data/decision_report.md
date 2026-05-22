# Decision Report

- generated_at: 2026-05-22T17:59:22.254476+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4731**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.32% / filled 20/20。**
- 全期間 MARKET基準: n=4731, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+0.32%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.32% | **+0.32%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 17/20 | 85.0% | +1.56% | **+1.32%** |
| LIMIT_9PCT | 6/20 | 30.0% | +4.29% | **+1.29%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.97% | **+0.87%** |
| LIMIT_10PCT | 4/20 | 20.0% | +3.73% | **+0.75%** |
| LIMIT_ATR | 9/20 | 45.0% | +1.62% | **+0.73%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 13/20 | 65.0% | +3.12% | **+2.03%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +2.88% | **+1.44%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +2.51% | **+1.00%** |
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +3.29% | **+0.82%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +2.55% | **+0.76%** |

## 2. $100 Live Portfolio

- 残高: **$95.25** / 初期 $100.00 (-4.75%)
- 確定トレード: 60件 (TP 15 / SL 42 / EXP 3)
- 最新: STXSTOCK/USDT:USDT SL_HIT PnL -1.86% 残高後 $95.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$125.68** / 初期 $100.00 (+25.68%)
- 確定: 577件 (Win 149 / Loss 187 / Flat 241) / skip 715件
- 成長率目線: 平均log +0.000396 / 幾何平均 +0.040% per trade / maxDD +4.21%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BEAT/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $125.68

## 4. Latest Market Context

- 更新: 2026-05-22T17:59:17.001571+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.25% price=76721.8
- Funnel: target 765 → liquid 136 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +64.45% | $32,036,455.71 |
| BEAT/USDT:USDT | +10.43% | $34,194,062.66 |
| GUA/USDT:USDT | +5.79% | $1,100,719.68 |
| BILL/USDT:USDT | +5.30% | $13,732,260.04 |
| INJ/USDT:USDT | +3.63% | $37,346,735.63 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEAT/USDT:USDT | below_1h_threshold | +3.67% | +3.92% |
| GUA/USDT:USDT | below_1h_threshold | +2.54% | +2.79% |
| UB/USDT:USDT | below_1h_threshold | +2.27% | +2.52% |
| FIDA/USDT:USDT | below_1h_threshold | +2.13% | +2.38% |
| INJ/USDT:USDT | below_1h_threshold | +2.06% | +2.31% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
