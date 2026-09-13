# Decision Report

- generated_at: 2026-09-13T18:16:18.562046+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14461**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14461, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.37%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.37% | **-0.37%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +4.06% | **+1.02%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_1PCT | 20/20 | 100.0% | +0.68% | **+0.68%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/5 | 60.0% | +3.90% | **+2.34%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +3.53% | **+1.59%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +2.13% | **+1.28%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.40% | **+0.91%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +0.90% | **+0.49%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 211件 (TP 78 / SL 128 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,075.03** / 初期 $100.00 (+975.03%)
- 確定: 5433件 (Win 1635 / Loss 1761 / Flat 2037) / skip 5589件
- 成長率目線: 平均log +0.000437 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ZCAT/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,075.03

## 4. Robust Adaptive DryRun ($100)

- 残高: **$231.25** / 初期 $100.00 (+131.25%)
- 確定: 2979件 (Win 829 / Loss 710 / Flat 1440) / skip 4893件
- 成長率目線: 平均log +0.000281 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1172 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AR/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $231.25

## 5. Causal Adaptive DryRun ($100)

- 残高: **$126.72** / 初期 $100.00 (+26.72%)
- 確定: 2856件 (Win 850 / Loss 1105 / Flat 901) / pending 0件 / skip 3076件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000423 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: REZ/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $126.72

## 6. Latest Market Context

- 更新: 2026-09-13T18:16:08.210492+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=77323.5
- Funnel: target 1068 → liquid 136 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PONS/USDT:USDT | +7.75% | $4,854,575.59 |
| AR/USDT:USDT | +6.81% | $2,063,639.34 |
| BTW/USDT:USDT | +6.00% | $7,532,430.95 |
| BR/USDT:USDT | +5.80% | $1,438,085.62 |
| NIULAI/USDT:USDT | +5.60% | $5,137,633.36 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FILECOIN/USDT:USDT | below_1h_threshold | +1.74% | +1.70% |
| AR/USDT:USDT | below_1h_threshold | +1.66% | +1.62% |
| LSK/USDT:USDT | below_1h_threshold | +1.18% | +1.14% |
| NBISSTOCK/USDT:USDT | below_1h_threshold | +1.16% | +1.12% |
| AKE/USDT:USDT | below_1h_threshold | +1.05% | +1.02% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
