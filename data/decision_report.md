# Decision Report

- generated_at: 2026-06-15T08:01:19.982314+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6761**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6761, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=-0.11%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.11% | **-0.11%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.48% | **+0.48%** |
| LIMIT_BB3S | 3/16 | 18.8% | +1.17% | **+0.22%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +0.69% | **+0.17%** |
| LIMIT_10PCT | 2/20 | 10.0% | +0.73% | **+0.07%** |
| MARKET | 20/20 | 100.0% | -0.11% | **-0.11%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/4 | 100.0% | +3.93% | **+3.93%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.69% | **+1.44%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +1.89% | **+1.32%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +2.03% | **+1.32%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +2.56% | **+0.89%** |

## 2. $100 Live Portfolio

- 残高: **$103.02** / 初期 $100.00 (+3.02%)
- 確定トレード: 6件 (TP 4 / SL 2 / EXP 0)
- 最新: RIF/USDT:USDT TP_HIT PnL +8.00% 残高後 $103.02
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$174.49** / 初期 $100.00 (+74.49%)
- 確定: 1634件 (Win 426 / Loss 505 / Flat 703) / skip 1688件
- 成長率目線: 平均log +0.000341 / 幾何平均 +0.034% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CLO/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $174.49

## 4. Robust Adaptive DryRun ($100)

- 残高: **$98.88** / 初期 $100.00 (-1.12%)
- 確定: 128件 (Win 25 / Loss 21 / Flat 82) / skip 44件
- 成長率目線: 平均log -0.000088 / 幾何平均 -0.009% per trade / maxDD +2.07%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_robust_growth_score) / robust_score +0.0055 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CLO/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $98.88

## 5. Latest Market Context

- 更新: 2026-06-15T08:01:15.030395+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=65619.8
- Funnel: target 770 → liquid 142 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ASTEROID/USDT:USDT | +101.22% | $3,943,177.23 |
| EVAA/USDT:USDT | +79.35% | $23,821,591.49 |
| CLO/USDT:USDT | +48.88% | $2,124,183.48 |
| PUFFER/USDT:USDT | +26.97% | $1,040,217.66 |
| GRASS/USDT:USDT | +22.63% | $2,024,562.68 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ETHFI/USDT:USDT | below_1h_threshold | +1.66% | +1.70% |
| ASTEROID/USDT:USDT | below_1h_threshold | +1.41% | +1.44% |
| UAI/USDT:USDT | below_1h_threshold | +0.71% | +0.74% |
| CLO/USDT:USDT | below_1h_threshold | +0.45% | +0.49% |
| SOXL/USDT:USDT | below_1h_threshold | +0.37% | +0.41% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
