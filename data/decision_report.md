# Decision Report

- generated_at: 2026-05-07T23:07:28.232209+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3714**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3714, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=+0.09%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.09% | **+0.09%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 7/20 | 35.0% | +2.03% | **+0.71%** |
| LIMIT_9PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_8PCT | 4/20 | 20.0% | +2.85% | **+0.57%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.61% | **+0.46%** |
| LIMIT_BB3S | 3/19 | 15.8% | +1.73% | **+0.27%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.56% | **+1.01%** |
| MARKET_LONG | 20/20 | 100.0% | +0.83% | **+0.83%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +2.67% | **+0.80%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +1.36% | **+0.68%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$99.32** / 初期 $100.00 (-0.68%)
- 確定トレード: 23件 (TP 6 / SL 15 / EXP 2)
- 最新: D/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.32
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.41** / 初期 $100.00 (+8.41%)
- 確定: 189件 (Win 48 / Loss 64 / Flat 77) / skip 86件
- 成長率目線: 平均log +0.000427 / 幾何平均 +0.043% per trade / maxDD +3.48%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FHE/USDT:USDT `LIMIT_4PCT_LONG` SL_HIT account -0.50% 残高後 $108.41

## 4. Latest Market Context

- 更新: 2026-05-07T23:07:25.482884+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=79933.6
- Funnel: target 766 → liquid 182 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +53.64% | $7,896,159.36 |
| NIL/USDT:USDT | +49.85% | $23,407,609.67 |
| TST/USDT:USDT | +25.62% | $5,906,874.99 |
| LAB/USDT:USDT | +18.30% | $222,467,673.35 |
| DYDX/USDT:USDT | +16.73% | $9,889,685.19 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BSB/USDT:USDT | below_1h_threshold | +1.41% | +1.33% |
| D/USDT:USDT | below_1h_threshold | +0.96% | +0.89% |
| CHIP/USDT:USDT | below_1h_threshold | +0.80% | +0.73% |
| HIGH/USDT:USDT | below_1h_threshold | +0.75% | +0.68% |
| B/USDT:USDT | below_1h_threshold | +0.75% | +0.67% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
