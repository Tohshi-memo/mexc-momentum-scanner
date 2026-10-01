# Decision Report

- generated_at: 2026-10-01T19:01:32.741419+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15933**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15933, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.19%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.19% | **-0.19%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 6/20 | 30.0% | +5.40% | **+1.62%** |
| LIMIT_8PCT | 3/20 | 15.0% | +6.57% | **+0.99%** |
| LIMIT_6PCT | 6/20 | 30.0% | +2.91% | **+0.87%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.95% | **+0.38%** |
| LIMIT_ATR | 10/20 | 50.0% | +0.39% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +2.19% | **+1.53%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +1.64% | **+0.98%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.40% | **+0.84%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +1.66% | **+0.83%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.99% | **+0.79%** |

## 2. $100 Live Portfolio

- 残高: **$120.63** / 初期 $100.00 (+20.63%)
- 確定トレード: 226件 (TP 82 / SL 137 / EXP 7)
- 最新: LONGXIA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.63
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,297.72** / 初期 $100.00 (+1197.72%)
- 確定: 6042件 (Win 1791 / Loss 1948 / Flat 2303) / skip 6452件
- 成長率目線: 平均log +0.000424 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LONGXIA/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $1,297.72

## 4. Robust Adaptive DryRun ($100)

- 残高: **$278.04** / 初期 $100.00 (+178.04%)
- 確定: 3586件 (Win 1000 / Loss 832 / Flat 1754) / skip 5758件
- 成長率目線: 平均log +0.000285 / 幾何平均 +0.029% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1166 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LONGXIA/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $278.04

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4100件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000343 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-01T19:01:21.393403+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=84787.7
- Funnel: target 1097 → liquid 168 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LONGXIA/USDT:USDT | +12.52% | $10,662,011.96 |
| MOVR/USDT:USDT | +9.24% | $26,386,628.38 |
| SI/USDT:USDT | +8.83% | $5,519,920.31 |
| MUU/USDT:USDT | +7.75% | $20,320,453.16 |
| USELESS/USDT:USDT | +7.01% | $3,389,612.31 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| KORU/USDT:USDT | below_1h_threshold | +1.25% | +1.23% |
| SKHYSTOCK/USDT:USDT | below_1h_threshold | +0.95% | +0.92% |
| NVIDIA/USDT:USDT | below_1h_threshold | +0.78% | +0.75% |
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +0.67% | +0.64% |
| SOXL/USDT:USDT | below_1h_threshold | +0.66% | +0.63% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
