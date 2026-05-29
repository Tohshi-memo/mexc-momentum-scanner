# Decision Report

- generated_at: 2026-05-29T15:54:58.516082+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5057**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5057, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 7/13 | 53.8% | +1.05% | **+0.57%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.61% | **+0.52%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.46% | **+0.41%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +1.48% | **+0.37%** |
| LIMIT_5PCT | 4/20 | 20.0% | +1.48% | **+0.30%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +3.46% | **+1.38%** |
| LIMIT_BB3S_LONG | 3/7 | 42.9% | +3.15% | **+1.35%** |
| LIMIT_FIB1272_LONG | 3/20 | 15.0% | +3.42% | **+0.51%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +3.28% | **+0.33%** |

## 2. $100 Live Portfolio

- 残高: **$98.60** / 初期 $100.00 (-1.40%)
- 確定トレード: 74件 (TP 22 / SL 49 / EXP 3)
- 最新: LIT/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.60
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$125.68** / 初期 $100.00 (+25.68%)
- 確定: 740件 (Win 175 / Loss 226 / Flat 339) / skip 878件
- 成長率目線: 平均log +0.000309 / 幾何平均 +0.031% per trade / maxDD +4.72%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CTR/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $125.68

## 4. Latest Market Context

- 更新: 2026-05-29T15:54:56.345844+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.95% price=73759.4
- Funnel: target 777 → liquid 154 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=2, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ALLO/USDT:USDT | +145.83% | $127,042,559.97 |
| HEI/USDT:USDT | +87.05% | $4,104,741.98 |
| ID/USDT:USDT | +44.36% | $3,266,135.73 |
| LAB/USDT:USDT | +25.82% | $96,304,770.05 |
| DELLSTOCK/USDT:USDT | +24.43% | $11,216,386.86 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LIT/USDT:USDT | below_relative_strength | +5.38% | +4.43% |
| ZBCN/USDT:USDT | below_relative_strength | +5.16% | +4.21% |
| USELESS/USDT:USDT | below_1h_threshold | +4.98% | +4.03% |
| AR/USDT:USDT | below_1h_threshold | +4.80% | +3.85% |
| INJ/USDT:USDT | below_1h_threshold | +4.26% | +3.31% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
