# Decision Report

- generated_at: 2026-08-22T04:52:01.814630+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12319**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12319, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.23%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.23% | **-1.23%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 6/20 | 30.0% | +2.83% | **+0.85%** |
| LIMIT_2PCT | 19/20 | 95.0% | +0.52% | **+0.49%** |
| LIMIT_3PCT | 17/20 | 85.0% | +0.46% | **+0.39%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.24% | **+0.09%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 11/20 | 55.0% | +3.34% | **+1.84%** |
| MARKET_LONG | 20/20 | 100.0% | +1.82% | **+1.82%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.95% | **+1.46%** |
| LIMIT_6PCT_LONG | 5/20 | 25.0% | +5.60% | **+1.40%** |
| LIMIT_BB3S_LONG | 5/12 | 41.7% | +2.82% | **+1.17%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 190件 (TP 72 / SL 113 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$727.59** / 初期 $100.00 (+627.59%)
- 確定: 4437件 (Win 1361 / Loss 1446 / Flat 1630) / skip 4443件
- 成長率目線: 平均log +0.000447 / 幾何平均 +0.045% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BEAT/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $727.59

## 4. Robust Adaptive DryRun ($100)

- 残高: **$157.80** / 初期 $100.00 (+57.80%)
- 確定: 1925件 (Win 530 / Loss 459 / Flat 936) / skip 3805件
- 成長率目線: 平均log +0.000237 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.2065 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BEAT/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $157.80

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.49** / 初期 $100.00 (+18.49%)
- 確定: 1854件 (Win 549 / Loss 698 / Flat 607) / pending 6件 / skip 1947件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000528 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CRO/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $118.49

## 6. Latest Market Context

- 更新: 2026-08-22T04:51:42.961051+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.21% price=78559.9
- Funnel: target 1018 → liquid 222 → pre 50 → checked 50 → surge 10 → strict 1
- Surge前reject: below_1h_threshold=38, below_relative_strength=2, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 91.2 >= 65=1, 4h RSI 86.0 >= 65=1, 4h RSI 89.7 >= 65=1, 4h RSI 90.5 >= 65=1, 4h RSI 77.5 >= 65=1, 4h RSI 91.1 >= 65=1, 4h RSI 79.8 >= 65=1, 4h RSI 86.6 >= 65=1, 4h RSI 80.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BASECAT/USDT:USDT | +248.45% | $4,471,288.16 |
| TRUMPOFFICIAL/USDT:USDT | +81.52% | $48,536,411.57 |
| CATE/USDT:USDT | +75.63% | $11,638,762.69 |
| MUBARAK/USDT:USDT | +34.60% | $1,546,293.30 |
| DASH/USDT:USDT | +27.09% | $17,014,083.19 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PEPE/USDT:USDT | below_relative_strength | +5.16% | +4.95% |
| POPCAT/USDT:USDT | below_relative_strength | +5.05% | +4.84% |
| POL/USDT:USDT | below_1h_threshold | +4.81% | +4.60% |
| ADA/USDT:USDT | below_1h_threshold | +4.51% | +4.30% |
| USELESS/USDT:USDT | below_1h_threshold | +4.43% | +4.22% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
