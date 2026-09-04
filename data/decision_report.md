# Decision Report

- generated_at: 2026-09-04T05:16:34.273123+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13583**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.33% / filled 20/20。**
- 全期間 MARKET基準: n=13583, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.33%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.33% | **+0.33%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 15/20 | 75.0% | +1.12% | **+0.84%** |
| LIMIT_3PCT | 14/20 | 70.0% | +1.06% | **+0.74%** |
| LIMIT_BB3S | 3/18 | 16.7% | +3.24% | **+0.54%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +1.11% | **+0.50%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.39% | **+0.33%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.21% | **+0.17%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.10% | **+0.16%** |
| MARKET_LONG | 20/20 | 100.0% | +0.08% | **+0.08%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +0.00% | **+0.00%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | -0.03% | **-0.01%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 199件 (TP 74 / SL 120 / EXP 5)
- 最新: MARSCOIN/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$859.66** / 初期 $100.00 (+759.66%)
- 確定: 5009件 (Win 1516 / Loss 1644 / Flat 1849) / skip 5135件
- 成長率目線: 平均log +0.000429 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BASECAT/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $859.66

## 4. Robust Adaptive DryRun ($100)

- 残高: **$185.77** / 初期 $100.00 (+85.77%)
- 確定: 2399件 (Win 680 / Loss 576 / Flat 1143) / skip 4595件
- 成長率目線: 平均log +0.000258 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0510 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BTR/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $185.77

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.59** / 初期 $100.00 (+16.59%)
- 確定: 2236件 (Win 666 / Loss 875 / Flat 695) / pending 6件 / skip 2814件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000149 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BTR/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.04% 残高後 $116.59

## 6. Latest Market Context

- 更新: 2026-09-04T05:16:22.559216+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.12% price=80942.2
- Funnel: target 1046 → liquid 164 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HNT/USDT:USDT | +25.39% | $12,062,275.77 |
| TRIA/USDT:USDT | +20.92% | $2,612,748.09 |
| BTR/USDT:USDT | +19.09% | $9,291,182.91 |
| USELESS/USDT:USDT | +18.15% | $30,331,424.16 |
| PROM/USDT:USDT | +15.38% | $2,560,571.47 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZEST/USDT:USDT | below_1h_threshold | +4.04% | +4.16% |
| MARSCOIN/USDT:USDT | below_1h_threshold | +2.03% | +2.15% |
| HNT/USDT:USDT | below_1h_threshold | +1.75% | +1.87% |
| TRIA/USDT:USDT | below_1h_threshold | +1.73% | +1.85% |
| KORU/USDT:USDT | below_1h_threshold | +1.56% | +1.68% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
