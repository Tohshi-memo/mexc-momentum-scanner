# Decision Report

- generated_at: 2026-07-12T23:01:10.285953+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8616**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.50% / filled 20/20。**
- 全期間 MARKET基準: n=8616, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.50%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.50% | **+1.50%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.50% | **+1.50%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.17% | **+1.05%** |
| LIMIT_2PCT | 16/20 | 80.0% | +1.30% | **+1.04%** |
| LIMIT_5PCT | 5/20 | 25.0% | +1.37% | **+0.34%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.27% | **+0.34%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/8 | 62.5% | +0.67% | **+0.42%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +0.45% | **+0.33%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.10% | **+0.07%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +0.06% | **+0.04%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | -0.03% | **-0.02%** |

## 2. $100 Live Portfolio

- 残高: **$101.71** / 初期 $100.00 (+1.71%)
- 確定トレード: 90件 (TP 30 / SL 58 / EXP 2)
- 最新: PIPPIN/USDT:USDT SL_HIT PnL -2.19% 残高後 $101.71
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$323.01** / 初期 $100.00 (+223.01%)
- 確定: 2791件 (Win 876 / Loss 922 / Flat 993) / skip 2386件
- 成長率目線: 平均log +0.000420 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: T/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $323.01

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.11** / 初期 $100.00 (+5.11%)
- 確定: 644件 (Win 152 / Loss 159 / Flat 333) / skip 1383件
- 成長率目線: 平均log +0.000077 / 幾何平均 +0.008% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VANRY/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $105.11

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.00** / 初期 $100.00 (-1.00%)
- 確定: 27件 (Win 9 / Loss 18 / Flat 0) / pending 0件 / skip 59件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000433 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $99.00

## 6. Latest Market Context

- 更新: 2026-07-12T23:01:03.058219+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=63809.8
- Funnel: target 863 → liquid 134 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DODO/USDT:USDT | +43.61% | $3,127,931.70 |
| BLAST/USDT:USDT | +29.27% | $1,600,690.69 |
| ANSEM/USDT:USDT | +6.15% | $3,837,354.82 |
| PIPPIN/USDT:USDT | +4.49% | $7,213,707.36 |
| FHE/USDT:USDT | +4.08% | $2,853,983.79 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UB/USDT:USDT | below_1h_threshold | +0.31% | +0.38% |
| BXSTOCK/USDT:USDT | below_1h_threshold | +0.30% | +0.37% |
| BASED/USDT:USDT | below_1h_threshold | +0.05% | +0.12% |
| OPENAI/USDT:USDT | below_1h_threshold | +0.03% | +0.10% |
| KORU/USDT:USDT | below_1h_threshold | +0.03% | +0.10% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
