# Decision Report

- generated_at: 2026-08-01T16:47:08.607754+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10103**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10103, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.38%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.38% | **-0.38%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_1PCT | 20/20 | 100.0% | +0.58% | **+0.58%** |
| LIMIT_2PCT | 18/20 | 90.0% | +0.48% | **+0.43%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +4.32% | **+0.43%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.13% | **+0.04%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +2.58% | **+1.93%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.28% | **+1.02%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +1.68% | **+0.92%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +0.95% | **+0.57%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +0.45% | **+0.34%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$570.82** / 初期 $100.00 (+470.82%)
- 確定: 3638件 (Win 1158 / Loss 1191 / Flat 1289) / skip 3026件
- 成長率目線: 平均log +0.000479 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BTW/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $570.82

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.81** / 初期 $100.00 (+40.81%)
- 確定: 1279件 (Win 359 / Loss 297 / Flat 623) / skip 2235件
- 成長率目線: 平均log +0.000268 / 幾何平均 +0.027% per trade / maxDD +3.89%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KOMA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $140.81

## 5. Causal Adaptive DryRun ($100)

- 残高: **$111.34** / 初期 $100.00 (+11.34%)
- 確定: 913件 (Win 289 / Loss 357 / Flat 267) / pending 6件 / skip 659件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000208 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.34% 残高後 $111.34

## 6. Latest Market Context

- 更新: 2026-08-01T16:46:43.485744+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=62932.9
- Funnel: target 922 → liquid 141 → pre 50 → checked 50 → surge 7 → strict 4
- Surge前reject: below_1h_threshold=43, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 84.0 >= 65=1, 4h RSI 82.9 >= 65=1, 4h RSI 66.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AEVO/USDT:USDT | +14.47% | $1,219,455.25 |
| UAI/USDT:USDT | +10.72% | $7,016,454.59 |
| IDOL/USDT:USDT | +8.21% | $1,517,741.81 |
| AKE/USDT:USDT | +8.07% | $17,228,799.35 |
| 1000RATS/USDT:USDT | +7.60% | $22,819,720.23 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GIGGLE/USDT:USDT | below_1h_threshold | +3.69% | +3.76% |
| ICNT/USDT:USDT | below_1h_threshold | +3.52% | +3.59% |
| ON/USDT:USDT | below_1h_threshold | +3.28% | +3.35% |
| US/USDT:USDT | below_1h_threshold | +2.27% | +2.34% |
| BLESS/USDT:USDT | below_1h_threshold | +1.92% | +1.99% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
