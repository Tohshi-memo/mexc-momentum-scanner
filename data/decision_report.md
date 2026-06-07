# Decision Report

- generated_at: 2026-06-07T17:04:22.007574+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5986**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5986, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 4/20 | 20.0% | +1.10% | **+0.22%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_5PCT | 9/20 | 45.0% | -0.15% | **-0.07%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +2.24% | **+1.57%** |
| LIMIT_FIB1272_LONG | 5/20 | 25.0% | +6.02% | **+1.50%** |
| MARKET_LONG | 20/20 | 100.0% | +1.40% | **+1.40%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +2.03% | **+1.12%** |
| ASK_LONG | 20/20 | 100.0% | +1.05% | **+1.05%** |

## 2. $100 Live Portfolio

- 残高: **$99.00** / 初期 $100.00 (-1.00%)
- 確定トレード: 5件 (TP 1 / SL 4 / EXP 0)
- 最新: BSB/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.00
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$150.53** / 初期 $100.00 (+50.53%)
- 確定: 1103件 (Win 267 / Loss 331 / Flat 505) / skip 1444件
- 成長率目線: 平均log +0.000371 / 幾何平均 +0.037% per trade / maxDD +7.25%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $150.53

## 4. Latest Market Context

- 更新: 2026-06-07T17:04:19.103418+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=62103.0
- Funnel: target 768 → liquid 121 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BANK/USDT:USDT | +23.56% | $1,666,254.38 |
| VELVET/USDT:USDT | +12.05% | $2,600,560.12 |
| LAB/USDT:USDT | +9.49% | $62,002,284.25 |
| BEAT/USDT:USDT | +9.30% | $49,391,398.45 |
| ALLO/USDT:USDT | +5.18% | $69,509,425.42 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +2.88% | +2.80% |
| SIREN/USDT:USDT | below_1h_threshold | +1.98% | +1.90% |
| BEAT/USDT:USDT | below_1h_threshold | +1.43% | +1.35% |
| H/USDT:USDT | below_1h_threshold | +1.41% | +1.33% |
| JTO/USDT:USDT | below_1h_threshold | +1.22% | +1.14% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
