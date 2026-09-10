# Decision Report

- generated_at: 2026-09-10T02:36:58.849814+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14143**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14143, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.13%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.13% | **-0.13%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 6/20 | 30.0% | +3.92% | **+1.18%** |
| LIMIT_5PCT | 10/20 | 50.0% | +2.08% | **+1.04%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +1.41% | **+0.57%** |
| LIMIT_8PCT | 3/20 | 15.0% | +3.70% | **+0.56%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +3.08% | **+2.46%** |
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +2.59% | **+2.33%** |
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +2.00% | **+1.33%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +1.20% | **+1.20%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.63% | **+0.98%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,037.63** / 初期 $100.00 (+937.63%)
- 確定: 5323件 (Win 1600 / Loss 1717 / Flat 2006) / skip 5381件
- 成長率目線: 平均log +0.000440 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CATE/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +1.00% 残高後 $1,037.63

## 4. Robust Adaptive DryRun ($100)

- 残高: **$204.64** / 初期 $100.00 (+104.64%)
- 確定: 2737件 (Win 756 / Loss 641 / Flat 1340) / skip 4817件
- 成長率目線: 平均log +0.000262 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0729 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.69% 残高後 $204.64

## 5. Causal Adaptive DryRun ($100)

- 残高: **$121.31** / 初期 $100.00 (+21.31%)
- 確定: 2648件 (Win 780 / Loss 1011 / Flat 857) / pending 5件 / skip 2962件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000483 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.34% 残高後 $121.31

## 6. Latest Market Context

- 更新: 2026-09-10T02:36:46.055239+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=78126.7
- Funnel: target 1064 → liquid 169 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.8 >= 65=1, 4h RSI 87.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VTHO/USDT:USDT | +47.45% | $1,655,625.10 |
| CATE/USDT:USDT | +27.71% | $2,854,013.85 |
| BTR/USDT:USDT | +21.08% | $2,536,760.97 |
| MINA/USDT:USDT | +2.85% | $1,336,703.99 |
| KAS/USDT:USDT | +2.78% | $4,096,727.25 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MINA/USDT:USDT | below_1h_threshold | +2.19% | +2.10% |
| INJ/USDT:USDT | below_1h_threshold | +1.27% | +1.19% |
| WLFI/USDT:USDT | below_1h_threshold | +1.13% | +1.04% |
| BR/USDT:USDT | below_1h_threshold | +1.11% | +1.02% |
| BULLA/USDT:USDT | below_1h_threshold | +1.10% | +1.02% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
