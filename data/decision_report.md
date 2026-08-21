# Decision Report

- generated_at: 2026-08-21T04:01:21.095827+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12145**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12145, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 6/20 | 30.0% | +3.67% | **+1.10%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.89% | **+0.66%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_4PCT | 15/20 | 75.0% | +0.53% | **+0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 11/20 | 55.0% | +3.55% | **+1.95%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +3.28% | **+1.64%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +3.97% | **+1.59%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +4.11% | **+1.44%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +2.00% | **+1.00%** |

## 2. $100 Live Portfolio

- 残高: **$121.29** / 初期 $100.00 (+21.29%)
- 確定トレード: 188件 (TP 72 / SL 111 / EXP 5)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.29
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$650.45** / 初期 $100.00 (+550.45%)
- 確定: 4356件 (Win 1337 / Loss 1430 / Flat 1589) / skip 4350件
- 成長率目線: 平均log +0.000430 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CATE/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $650.45

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.16** / 初期 $100.00 (+54.16%)
- 確定: 1823件 (Win 502 / Loss 429 / Flat 892) / skip 3733件
- 成長率目線: 平均log +0.000237 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.0573 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $154.16

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.21** / 初期 $100.00 (+17.21%)
- 確定: 1822件 (Win 540 / Loss 691 / Flat 591) / pending 2件 / skip 1796件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000216 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ONG/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $117.21

## 6. Latest Market Context

- 更新: 2026-08-21T04:01:14.265014+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.14% price=74587.9
- Funnel: target 1011 → liquid 193 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +107.95% | $4,887,144.73 |
| ONG/USDT:USDT | +76.49% | $35,165,526.87 |
| ENA/USDT:USDT | +22.08% | $56,087,170.36 |
| ONT/USDT:USDT | +20.46% | $3,734,900.74 |
| CRV/USDT:USDT | +19.93% | $7,989,451.93 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HEMI/USDT:USDT | below_1h_threshold | +0.91% | +0.77% |
| CHIP/USDT:USDT | below_1h_threshold | +0.61% | +0.47% |
| KIOXIASTOCK/USDT:USDT | below_1h_threshold | +0.58% | +0.44% |
| SPX/USDT:USDT | below_1h_threshold | +0.53% | +0.39% |
| UNITREE/USDT:USDT | below_1h_threshold | +0.51% | +0.37% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
