# Decision Report

- generated_at: 2026-10-26T05:41:09.428669+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17464**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.00% / filled 20/20。**
- 全期間 MARKET基準: n=17464, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+2.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.00% | **+2.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.00% | **+2.00%** |
| LIMIT_8PCT | 4/20 | 20.0% | +5.85% | **+1.17%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.18% | **+1.01%** |
| LIMIT_ATR | 6/20 | 30.0% | +3.25% | **+0.98%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +4.21% | **+0.84%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +0.29% | **+0.20%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +0.25% | **+0.07%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +0.13% | **+0.03%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | -0.04% | **-0.02%** |

## 2. $100 Live Portfolio

- 残高: **$121.74** / 初期 $100.00 (+21.74%)
- 確定トレード: 251件 (TP 93 / SL 150 / EXP 8)
- 最新: CT/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.74
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,550.06** / 初期 $100.00 (+1450.06%)
- 確定: 6717件 (Win 1956 / Loss 2149 / Flat 2612) / skip 7308件
- 成長率目線: 平均log +0.000408 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AXIS/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $1,550.06

## 4. Robust Adaptive DryRun ($100)

- 残高: **$315.96** / 初期 $100.00 (+215.96%)
- 確定: 4007件 (Win 1111 / Loss 948 / Flat 1948) / skip 6868件
- 成長率目線: 平均log +0.000287 / 幾何平均 +0.029% per trade / maxDD +4.13%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0281 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AXIS/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $315.96

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5623件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000185 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-26T05:41:00.304695+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=80143.9
- Funnel: target 1070 → liquid 144 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| KIMCHI/USDT:USDT | +42.00% | $2,948,960.70 |
| RLS/USDT:USDT | +17.85% | $1,049,369.95 |
| BR/USDT:USDT | +11.44% | $8,461,365.67 |
| DODO/USDT:USDT | +10.24% | $1,179,943.61 |
| CLAUDIA/USDT:USDT | +8.40% | $1,117,385.33 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NIL/USDT:USDT | below_1h_threshold | +3.18% | +3.12% |
| CLAUDIA/USDT:USDT | below_1h_threshold | +2.02% | +1.97% |
| QNT/USDT:USDT | below_1h_threshold | +1.88% | +1.83% |
| CHIP/USDT:USDT | below_1h_threshold | +1.56% | +1.51% |
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +1.33% | +1.28% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
