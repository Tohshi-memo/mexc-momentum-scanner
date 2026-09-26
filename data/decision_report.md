# Decision Report

- generated_at: 2026-09-26T02:56:22.149623+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15561**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15561, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.08%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.08% | **+0.08%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +1.25% | **+1.18%** |
| LIMIT_BB3S | 4/20 | 20.0% | +3.37% | **+0.67%** |
| LIMIT_8PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_3PCT | 13/20 | 65.0% | +0.40% | **+0.26%** |
| LIMIT_ATR | 10/20 | 50.0% | +0.48% | **+0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +3.10% | **+1.24%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.45% | **+0.80%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +2.55% | **+0.76%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.72% | **+0.68%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +2.00% | **+0.60%** |

## 2. $100 Live Portfolio

- 残高: **$120.79** / 初期 $100.00 (+20.79%)
- 確定トレード: 223件 (TP 82 / SL 135 / EXP 6)
- 最新: BATON/USDT:USDT TP_HIT PnL +8.00% 残高後 $120.79
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,205.09** / 初期 $100.00 (+1105.09%)
- 確定: 5923件 (Win 1746 / Loss 1899 / Flat 2278) / skip 6199件
- 成長率目線: 平均log +0.000420 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ARK/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.80% 残高後 $1,205.09

## 4. Robust Adaptive DryRun ($100)

- 残高: **$255.25** / 初期 $100.00 (+155.25%)
- 確定: 3493件 (Win 956 / Loss 795 / Flat 1742) / skip 5479件
- 成長率目線: 平均log +0.000268 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0597 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ARK/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $255.25

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.38** / 初期 $100.00 (+19.38%)
- 確定: 3184件 (Win 936 / Loss 1262 / Flat 986) / pending 2件 / skip 3845件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000258 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ARK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $119.38

## 6. Latest Market Context

- 更新: 2026-09-26T02:56:11.098396+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=83993.8
- Funnel: target 1067 → liquid 170 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BATON/USDT:USDT | +30.76% | $1,445,935.61 |
| PHA/USDT:USDT | +15.82% | $28,122,184.12 |
| BR/USDT:USDT | +15.59% | $9,773,845.48 |
| ARK/USDT:USDT | +15.13% | $2,874,612.08 |
| AERO/USDT:USDT | +12.27% | $3,558,329.68 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AERO/USDT:USDT | below_1h_threshold | +4.66% | +4.72% |
| ARK/USDT:USDT | below_1h_threshold | +4.39% | +4.45% |
| BP/USDT:USDT | below_1h_threshold | +1.97% | +2.03% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +1.86% | +1.92% |
| ONE/USDT:USDT | below_1h_threshold | +1.39% | +1.44% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
