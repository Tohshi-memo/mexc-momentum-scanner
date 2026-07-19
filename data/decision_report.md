# Decision Report

- generated_at: 2026-07-19T02:06:06.724318+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8993**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8993, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-2.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.80% | **-2.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +6.73% | **+0.67%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_8PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_FIB1618 | 4/20 | 20.0% | +2.35% | **+0.47%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +3.34% | **+2.67%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +4.22% | **+2.53%** |
| MARKET_LONG | 20/20 | 100.0% | +2.20% | **+2.20%** |
| LIMIT_ATR_LONG | 7/20 | 35.0% | +5.64% | **+1.98%** |
| LIMIT_3PCT_LONG | 8/20 | 40.0% | +4.71% | **+1.88%** |

## 2. $100 Live Portfolio

- 残高: **$110.80** / 初期 $100.00 (+10.80%)
- 確定トレード: 117件 (TP 43 / SL 69 / EXP 5)
- 最新: SKYAI/USDT:USDT EXPIRED PnL +0.79% 残高後 $110.80
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$374.32** / 初期 $100.00 (+274.32%)
- 確定: 3056件 (Win 951 / Loss 973 / Flat 1132) / skip 2498件
- 成長率目線: 平均log +0.000432 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $374.32

## 4. Robust Adaptive DryRun ($100)

- 残高: **$123.77** / 初期 $100.00 (+23.77%)
- 確定: 954件 (Win 241 / Loss 192 / Flat 521) / skip 1450件
- 成長率目線: 平均log +0.000224 / 幾何平均 +0.022% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.2486 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.52% 残高後 $123.77

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.64** / 初期 $100.00 (-0.36%)
- 確定: 199件 (Win 64 / Loss 107 / Flat 28) / pending 1件 / skip 264件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000670 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $99.64

## 6. Latest Market Context

- 更新: 2026-07-19T02:06:02.294444+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=64807.9
- Funnel: target 885 → liquid 123 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +104.26% | $32,260,533.55 |
| BANK/USDT:USDT | +39.19% | $18,541,664.96 |
| B/USDT:USDT | +25.51% | $33,300,955.27 |
| TLM/USDT:USDT | +20.24% | $2,966,686.88 |
| AKE/USDT:USDT | +18.05% | $84,067,114.69 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| B/USDT:USDT | below_1h_threshold | +1.66% | +1.57% |
| BANK/USDT:USDT | below_1h_threshold | +1.09% | +1.00% |
| ANSEM/USDT:USDT | below_1h_threshold | +0.82% | +0.73% |
| MYX/USDT:USDT | below_1h_threshold | +0.70% | +0.61% |
| WLD/USDT:USDT | below_1h_threshold | +0.69% | +0.60% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
