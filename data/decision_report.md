# Decision Report

- generated_at: 2026-08-30T04:06:22.000645+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13008**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13008, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.75%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.75% | **-1.75%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 4/20 | 20.0% | +3.70% | **+0.74%** |
| LIMIT_6PCT | 4/20 | 20.0% | +3.47% | **+0.69%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_4PCT | 16/20 | 80.0% | +0.50% | **+0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 14/20 | 70.0% | +3.96% | **+2.77%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +5.79% | **+2.60%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +4.25% | **+2.55%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +2.87% | **+1.72%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.77% | **+1.33%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 194件 (TP 73 / SL 116 / EXP 5)
- 最新: SKR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$790.06** / 初期 $100.00 (+690.06%)
- 確定: 4778件 (Win 1458 / Loss 1573 / Flat 1747) / skip 4791件
- 成長率目線: 平均log +0.000433 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BICO/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $790.06

## 4. Robust Adaptive DryRun ($100)

- 残高: **$172.92** / 初期 $100.00 (+72.92%)
- 確定: 2092件 (Win 585 / Loss 509 / Flat 998) / skip 4327件
- 成長率目線: 平均log +0.000262 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1175 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BICO/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $172.92

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.63** / 初期 $100.00 (+16.63%)
- 確定: 2053件 (Win 604 / Loss 798 / Flat 651) / pending 5件 / skip 2424件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000442 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: HNT/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $116.63

## 6. Latest Market Context

- 更新: 2026-08-30T04:06:12.708120+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.11% price=78185.5
- Funnel: target 1023 → liquid 116 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NIULAI/USDT:USDT | +70.36% | $2,097,865.20 |
| PONS/USDT:USDT | +44.22% | $1,446,981.14 |
| HNT/USDT:USDT | +44.03% | $28,057,586.17 |
| FONE/USDT:USDT | +32.30% | $1,282,797.37 |
| PROM/USDT:USDT | +25.97% | $13,945,985.47 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTR/USDT:USDT | below_1h_threshold | +2.23% | +2.12% |
| NIULAI/USDT:USDT | below_1h_threshold | +1.97% | +1.87% |
| MOVR/USDT:USDT | below_1h_threshold | +1.33% | +1.22% |
| BTW/USDT:USDT | below_1h_threshold | +0.89% | +0.78% |
| PONS/USDT:USDT | below_1h_threshold | +0.77% | +0.66% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
