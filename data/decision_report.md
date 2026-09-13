# Decision Report

- generated_at: 2026-09-13T21:46:10.829865+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14466**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14466, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.73%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.73% | **-0.73%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +2.53% | **+0.89%** |
| LIMIT_1PCT | 20/20 | 100.0% | +0.87% | **+0.87%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +3.90% | **+3.90%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +4.86% | **+2.19%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.13% | **+0.79%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +1.29% | **+0.71%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.23% | **+0.68%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 211件 (TP 78 / SL 128 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,075.03** / 初期 $100.00 (+975.03%)
- 確定: 5433件 (Win 1635 / Loss 1761 / Flat 2037) / skip 5594件
- 成長率目線: 平均log +0.000437 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ZCAT/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,075.03

## 4. Robust Adaptive DryRun ($100)

- 残高: **$231.64** / 初期 $100.00 (+131.64%)
- 確定: 2984件 (Win 830 / Loss 711 / Flat 1443) / skip 4893件
- 成長率目線: 平均log +0.000282 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1080 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LSK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.52% 残高後 $231.64

## 5. Causal Adaptive DryRun ($100)

- 残高: **$126.72** / 初期 $100.00 (+26.72%)
- 確定: 2856件 (Win 850 / Loss 1105 / Flat 901) / pending 0件 / skip 3081件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000389 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: REZ/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $126.72

## 6. Latest Market Context

- 更新: 2026-09-13T21:46:02.911932+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=77349.7
- Funnel: target 1068 → liquid 141 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 75.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| POWER/USDT:USDT | +20.39% | $2,205,359.90 |
| MAGMA/USDT:USDT | +11.35% | $1,694,906.24 |
| BTW/USDT:USDT | +9.46% | $9,196,579.10 |
| MEMEROBINHOOD/USDT:USDT | +8.69% | $1,075,353.07 |
| USELESS/USDT:USDT | +8.47% | $5,096,879.86 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| POWER/USDT:USDT | below_1h_threshold | +3.93% | +3.88% |
| BTW/USDT:USDT | below_1h_threshold | +2.34% | +2.29% |
| ICP/USDT:USDT | below_1h_threshold | +1.58% | +1.54% |
| RAY/USDT:USDT | below_1h_threshold | +1.08% | +1.03% |
| VTHO/USDT:USDT | below_1h_threshold | +0.87% | +0.83% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
