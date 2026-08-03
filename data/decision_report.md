# Decision Report

- generated_at: 2026-08-03T01:01:23.761452+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10182**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10182, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.91%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.91% | **-1.91%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_5PCT | 3/20 | 15.0% | -0.70% | **-0.10%** |
| LIMIT_ATR | 11/20 | 55.0% | -0.23% | **-0.13%** |
| LIMIT_4PCT | 16/20 | 80.0% | -0.25% | **-0.20%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | -1.57% | **-0.31%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +2.95% | **+2.36%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +2.26% | **+1.24%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.32% | **+1.12%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +2.79% | **+1.12%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +1.96% | **+1.08%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$566.31** / 初期 $100.00 (+466.31%)
- 確定: 3676件 (Win 1166 / Loss 1205 / Flat 1305) / skip 3067件
- 成長率目線: 平均log +0.000472 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BICO/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $566.31

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.31** / 初期 $100.00 (+40.31%)
- 確定: 1282件 (Win 359 / Loss 298 / Flat 625) / skip 2311件
- 成長率目線: 平均log +0.000264 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BLESS/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $140.31

## 5. Causal Adaptive DryRun ($100)

- 残高: **$112.22** / 初期 $100.00 (+12.22%)
- 確定: 969件 (Win 307 / Loss 380 / Flat 282) / pending 1件 / skip 681件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000176 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SYN/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $112.22

## 6. Latest Market Context

- 更新: 2026-08-03T01:01:16.312954+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.11% price=63229.8
- Funnel: target 922 → liquid 130 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BICO/USDT:USDT | +33.74% | $2,432,329.18 |
| 1000RATS/USDT:USDT | +33.34% | $36,577,740.00 |
| BLESS/USDT:USDT | +23.10% | $60,106,042.02 |
| TAKE/USDT:USDT | +12.06% | $1,049,989.70 |
| FHE/USDT:USDT | +8.18% | $1,571,969.06 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SOXS/USDT:USDT | below_1h_threshold | +3.50% | +3.61% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +1.50% | +1.60% |
| AXTISTOCK/USDT:USDT | below_1h_threshold | +1.49% | +1.60% |
| KORU/USDT:USDT | below_1h_threshold | +1.28% | +1.39% |
| NVIDIA/USDT:USDT | below_1h_threshold | +0.61% | +0.72% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
