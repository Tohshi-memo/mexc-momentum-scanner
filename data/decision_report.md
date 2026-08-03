# Decision Report

- generated_at: 2026-08-03T05:01:17.654193+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10189**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10189, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.69%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.69% | **-1.69%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_5PCT | 5/20 | 25.0% | +1.37% | **+0.34%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.96% | **+0.29%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.39% | **+0.25%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | -0.10% | **-0.03%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +3.19% | **+2.55%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +2.74% | **+1.64%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +2.87% | **+1.29%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +2.46% | **+0.99%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +2.74% | **+0.96%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$566.31** / 初期 $100.00 (+466.31%)
- 確定: 3676件 (Win 1166 / Loss 1205 / Flat 1305) / skip 3074件
- 成長率目線: 平均log +0.000472 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BICO/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $566.31

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.31** / 初期 $100.00 (+40.31%)
- 確定: 1282件 (Win 359 / Loss 298 / Flat 625) / skip 2318件
- 成長率目線: 平均log +0.000264 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0202 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BLESS/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $140.31

## 5. Causal Adaptive DryRun ($100)

- 残高: **$113.38** / 初期 $100.00 (+13.38%)
- 確定: 975件 (Win 311 / Loss 381 / Flat 283) / pending 5件 / skip 681件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000237 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: 1000RATS/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.34% 残高後 $113.38

## 6. Latest Market Context

- 更新: 2026-08-03T05:01:10.308729+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=62799.9
- Funnel: target 924 → liquid 140 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| 1000RATS/USDT:USDT | +51.67% | $35,599,739.04 |
| BLESS/USDT:USDT | +23.59% | $69,896,638.79 |
| BICO/USDT:USDT | +23.18% | $6,259,961.41 |
| TAKE/USDT:USDT | +18.78% | $1,184,666.37 |
| GRVT/USDT:USDT | +12.68% | $2,450,634.07 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SOXS/USDT:USDT | below_1h_threshold | +0.97% | +0.92% |
| FHE/USDT:USDT | below_1h_threshold | +0.59% | +0.53% |
| GIGGLE/USDT:USDT | below_1h_threshold | +0.41% | +0.36% |
| PIEVERSE/USDT:USDT | below_1h_threshold | +0.23% | +0.17% |
| ZEC/USDT:USDT | below_1h_threshold | +0.22% | +0.17% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
