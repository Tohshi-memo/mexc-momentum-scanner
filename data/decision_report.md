# Decision Report

- generated_at: 2026-07-24T13:51:12.920125+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9442**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9442, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 9/20 | 45.0% | +0.95% | **+0.43%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +1.55% | **+0.23%** |
| LIMIT_ATR | 11/20 | 55.0% | +0.06% | **+0.03%** |
| LIMIT_4PCT | 15/20 | 75.0% | +0.00% | **+0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.09% | **+0.87%** |
| MARKET_LONG | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +1.06% | **+0.64%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +0.46% | **+0.23%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +0.50% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$103.79** / 初期 $100.00 (+3.79%)
- 確定トレード: 136件 (TP 45 / SL 86 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -2.63% 残高後 $103.79
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$425.48** / 初期 $100.00 (+325.48%)
- 確定: 3324件 (Win 1048 / Loss 1076 / Flat 1200) / skip 2679件
- 成長率目線: 平均log +0.000436 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BANK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $425.48

## 4. Robust Adaptive DryRun ($100)

- 残高: **$130.36** / 初期 $100.00 (+30.36%)
- 確定: 1164件 (Win 312 / Loss 254 / Flat 598) / skip 1689件
- 成長率目線: 平均log +0.000228 / 幾何平均 +0.023% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1095 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BANK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $130.36

## 5. Causal Adaptive DryRun ($100)

- 残高: **$103.21** / 初期 $100.00 (+3.21%)
- 確定: 502件 (Win 167 / Loss 197 / Flat 138) / pending 2件 / skip 407件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000335 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $103.21

## 6. Latest Market Context

- 更新: 2026-07-24T13:51:07.765628+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.85% price=64197.6
- Funnel: target 898 → liquid 172 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +42.49% | $13,361,702.33 |
| PONS/USDT:USDT | +40.99% | $1,118,191.26 |
| LA/USDT:USDT | +23.79% | $2,022,805.94 |
| CAP/USDT:USDT | +22.35% | $1,640,225.83 |
| RE/USDT:USDT | +21.92% | $22,139,349.82 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LA/USDT:USDT | below_1h_threshold | +2.73% | +3.58% |
| NGAS/USDT:USDT | below_1h_threshold | +1.64% | +2.49% |
| CAP/USDT:USDT | below_1h_threshold | +1.52% | +2.37% |
| SOXS/USDT:USDT | below_1h_threshold | +1.31% | +2.16% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.20% | +2.04% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
