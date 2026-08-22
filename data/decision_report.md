# Decision Report

- generated_at: 2026-08-22T03:56:47.785788+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12305**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12305, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.49%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.49% | **-1.49%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 6/20 | 30.0% | +3.04% | **+0.91%** |
| LIMIT_8PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_6PCT | 5/20 | 25.0% | +0.71% | **+0.18%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.24% | **+0.09%** |
| LIMIT_4PCT | 15/20 | 75.0% | +0.00% | **+0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/7 | 57.1% | +5.39% | **+3.08%** |
| MARKET_LONG | 20/20 | 100.0% | +2.00% | **+2.00%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +2.20% | **+1.98%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +2.40% | **+1.32%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +2.38% | **+1.31%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 190件 (TP 72 / SL 113 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$710.27** / 初期 $100.00 (+610.27%)
- 確定: 4423件 (Win 1355 / Loss 1443 / Flat 1625) / skip 4443件
- 成長率目線: 平均log +0.000443 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TRUMPOFFICIAL/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $710.27

## 4. Robust Adaptive DryRun ($100)

- 残高: **$156.21** / 初期 $100.00 (+56.21%)
- 確定: 1911件 (Win 526 / Loss 456 / Flat 929) / skip 3805件
- 成長率目線: 平均log +0.000233 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.2484 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TRUMPOFFICIAL/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $156.21

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.39** / 初期 $100.00 (+18.39%)
- 確定: 1850件 (Win 548 / Loss 697 / Flat 605) / pending 6件 / skip 1934件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000566 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $118.39

## 6. Latest Market Context

- 更新: 2026-08-22T03:56:34.055039+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.07% price=78522.0
- Funnel: target 1018 → liquid 222 → pre 50 → checked 50 → surge 5 → strict 1
- Surge前reject: below_1h_threshold=45, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.5 >= 65=1, 4h RSI 75.4 >= 65=1, 4h RSI 87.1 >= 65=1, 4h RSI 88.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BASECAT/USDT:USDT | +223.71% | $4,213,564.87 |
| CATE/USDT:USDT | +68.11% | $12,019,882.28 |
| TRUMPOFFICIAL/USDT:USDT | +42.49% | $27,856,435.98 |
| MUBARAK/USDT:USDT | +33.54% | $1,343,629.80 |
| DASH/USDT:USDT | +31.88% | $16,048,188.32 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NIULAI/USDT:USDT | below_1h_threshold | +4.79% | +4.72% |
| OP/USDT:USDT | below_1h_threshold | +4.37% | +4.30% |
| ZEC/USDT:USDT | below_1h_threshold | +3.77% | +3.70% |
| 1000BONK/USDT:USDT | below_1h_threshold | +3.73% | +3.66% |
| JIMOTHY/USDT:USDT | below_1h_threshold | +3.70% | +3.63% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
