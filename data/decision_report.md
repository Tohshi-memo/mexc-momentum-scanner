# Decision Report

- generated_at: 2026-08-22T04:16:29.368039+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12310**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12310, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 4/20 | 20.0% | +4.44% | **+0.89%** |
| LIMIT_8PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_3PCT | 18/20 | 90.0% | +0.69% | **+0.62%** |
| LIMIT_2PCT | 19/20 | 95.0% | +0.23% | **+0.22%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.40% | **+0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.60% | **+1.60%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.69% | **+1.53%** |
| LIMIT_BB3S_LONG | 4/9 | 44.4% | +3.13% | **+1.39%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +2.25% | **+1.35%** |
| LIMIT_5PCT_LONG | 7/20 | 35.0% | +2.86% | **+1.00%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 190件 (TP 72 / SL 113 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$712.09** / 初期 $100.00 (+612.09%)
- 確定: 4428件 (Win 1357 / Loss 1445 / Flat 1626) / skip 4443件
- 成長率目線: 平均log +0.000443 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MUBARAK/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $712.09

## 4. Robust Adaptive DryRun ($100)

- 残高: **$156.60** / 初期 $100.00 (+56.60%)
- 確定: 1916件 (Win 528 / Loss 458 / Flat 930) / skip 3805件
- 成長率目線: 平均log +0.000234 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.2383 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MUBARAK/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $156.60

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.49** / 初期 $100.00 (+18.49%)
- 確定: 1853件 (Win 549 / Loss 698 / Flat 606) / pending 4件 / skip 1934件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000532 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $118.49

## 6. Latest Market Context

- 更新: 2026-08-22T04:16:18.789962+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=78337.8
- Funnel: target 1018 → liquid 219 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BASECAT/USDT:USDT | +244.32% | $4,288,463.82 |
| CATE/USDT:USDT | +65.42% | $11,498,573.93 |
| TRUMPOFFICIAL/USDT:USDT | +41.75% | $37,213,198.49 |
| MUBARAK/USDT:USDT | +39.22% | $1,403,205.60 |
| DASH/USDT:USDT | +28.77% | $16,326,828.91 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MUBARAK/USDT:USDT | below_1h_threshold | +4.40% | +4.48% |
| BASECAT/USDT:USDT | below_1h_threshold | +4.39% | +4.46% |
| WLD/USDT:USDT | below_1h_threshold | +3.27% | +3.34% |
| PEPE/USDT:USDT | below_1h_threshold | +3.23% | +3.30% |
| CRO/USDT:USDT | below_1h_threshold | +2.52% | +2.60% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
