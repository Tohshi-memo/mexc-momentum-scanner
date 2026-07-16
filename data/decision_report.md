# Decision Report

- generated_at: 2026-07-16T15:06:16.005669+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8811**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8811, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.74%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.74% | **-0.74%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.33% | **+0.13%** |
| LIMIT_ATR | 13/20 | 65.0% | -0.22% | **-0.14%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.24% | **+1.24%** |
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +1.19% | **+1.19%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +1.67% | **+1.00%** |
| LIMIT_8PCT_LONG | 4/20 | 20.0% | +4.42% | **+0.88%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.97% | **+0.60%** |

## 2. $100 Live Portfolio

- 残高: **$109.02** / 初期 $100.00 (+9.02%)
- 確定トレード: 106件 (TP 40 / SL 64 / EXP 2)
- 最新: DEXE/USDT:USDT TP_HIT PnL +8.00% 残高後 $109.02
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$339.63** / 初期 $100.00 (+239.63%)
- 確定: 2926件 (Win 912 / Loss 945 / Flat 1069) / skip 2446件
- 成長率目線: 平均log +0.000418 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MANTRA/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.26% 残高後 $339.63

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.12** / 初期 $100.00 (+7.12%)
- 確定: 773件 (Win 178 / Loss 170 / Flat 425) / skip 1449件
- 成長率目線: 平均log +0.000089 / 幾何平均 +0.009% per trade / maxDD +3.89%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0026 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MANTRA/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $107.12

## 5. Causal Adaptive DryRun ($100)

- 残高: **$97.77** / 初期 $100.00 (-2.23%)
- 確定: 80件 (Win 23 / Loss 53 / Flat 4) / pending 2件 / skip 198件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000323 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MANTRA/USDT:USDT `MARKET` TP_HIT account +0.34% 残高後 $97.77

## 6. Latest Market Context

- 更新: 2026-07-16T15:06:08.269646+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.11% price=64441.6
- Funnel: target 880 → liquid 167 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 84.7 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +63.30% | $6,772,354.57 |
| AKE/USDT:USDT | +28.55% | $40,016,772.50 |
| MANTRA/USDT:USDT | +20.90% | $2,265,551.86 |
| US/USDT:USDT | +20.54% | $15,645,245.92 |
| BANK/USDT:USDT | +16.91% | $4,982,236.41 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| US/USDT:USDT | below_1h_threshold | +1.45% | +1.55% |
| MSFTSTOCK/USDT:USDT | below_1h_threshold | +1.05% | +1.16% |
| ROAM/USDT:USDT | below_1h_threshold | +0.68% | +0.78% |
| RE/USDT:USDT | below_1h_threshold | +0.51% | +0.61% |
| BANK/USDT:USDT | below_1h_threshold | +0.48% | +0.59% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
