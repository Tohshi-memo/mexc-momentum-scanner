# Decision Report

- generated_at: 2026-06-13T19:17:22.772880+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6606**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6606, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +1.93% | **+0.48%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.25% | **+0.44%** |
| LIMIT_3PCT | 16/20 | 80.0% | +0.52% | **+0.42%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.29% | **+0.20%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +0.05% | **+0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 12/20 | 60.0% | +2.71% | **+1.63%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.14% | **+0.97%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.60% | **+0.64%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.61% | **+0.42%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$100.00** / 初期 $100.00 (+0.00%)
- 確定トレード: 0件 (TP 0 / SL 0 / EXP 0)

## 3. Safe Adaptive DryRun ($100)

- 残高: **$168.42** / 初期 $100.00 (+68.42%)
- 確定: 1479件 (Win 398 / Loss 470 / Flat 611) / skip 1688件
- 成長率目線: 平均log +0.000352 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MEGA/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $168.42

## 4. Robust Adaptive DryRun ($100)

- 残高: **$100.11** / 初期 $100.00 (+0.11%)
- 確定: 17件 (Win 6 / Loss 6 / Flat 5) / skip 0件
- 成長率目線: 平均log +0.000062 / 幾何平均 +0.006% per trade / maxDD +1.05%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0580 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MEGA/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $100.11

## 5. Latest Market Context

- 更新: 2026-06-13T19:17:18.129879+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=64148.9
- Funnel: target 770 → liquid 132 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +14.34% | $62,773,456.17 |
| RIF/USDT:USDT | +14.24% | $7,229,724.21 |
| AT/USDT:USDT | +12.49% | $1,031,187.61 |
| COAI/USDT:USDT | +6.58% | $25,058,359.35 |
| H/USDT:USDT | +5.86% | $15,282,017.27 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MEGA/USDT:USDT | below_1h_threshold | +4.14% | +4.10% |
| RIF/USDT:USDT | below_1h_threshold | +2.64% | +2.60% |
| AT/USDT:USDT | below_1h_threshold | +1.73% | +1.69% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.53% | +1.49% |
| JCT/USDT:USDT | below_1h_threshold | +1.25% | +1.21% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
