# Decision Report

- generated_at: 2026-08-19T10:51:26.312757+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11971**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11971, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.08%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.08% | **-0.08%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 3/20 | 15.0% | -0.08% | **-0.01%** |
| MARKET | 20/20 | 100.0% | -0.08% | **-0.08%** |
| LIMIT_5PCT | 3/20 | 15.0% | -0.70% | **-0.10%** |
| LIMIT_4PCT | 12/20 | 60.0% | -0.33% | **-0.20%** |
| LIMIT_BB3S | 2/16 | 12.5% | -1.80% | **-0.22%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.96% | **+0.82%** |
| MARKET_LONG | 20/20 | 100.0% | +0.52% | **+0.52%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +0.51% | **+0.31%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +0.58% | **+0.09%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +0.13% | **+0.04%** |

## 2. $100 Live Portfolio

- 残高: **$121.29** / 初期 $100.00 (+21.29%)
- 確定トレード: 188件 (TP 72 / SL 111 / EXP 5)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.29
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$622.90** / 初期 $100.00 (+522.90%)
- 確定: 4232件 (Win 1301 / Loss 1381 / Flat 1550) / skip 4300件
- 成長率目線: 平均log +0.000432 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BTW/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $622.90

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.70** / 初期 $100.00 (+54.70%)
- 確定: 1821件 (Win 502 / Loss 428 / Flat 891) / skip 3561件
- 成長率目線: 平均log +0.000240 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0453 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: UNITREE/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.35% 残高後 $154.70

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.79** / 初期 $100.00 (+17.79%)
- 確定: 1748件 (Win 520 / Loss 665 / Flat 563) / pending 2件 / skip 1691件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000123 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BTW/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $117.79

## 6. Latest Market Context

- 更新: 2026-08-19T10:51:19.260863+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=64390.3
- Funnel: target 992 → liquid 180 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 70.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTW/USDT:USDT | +78.96% | $88,090,526.69 |
| HEMI/USDT:USDT | +34.03% | $3,327,184.57 |
| UNITREE/USDT:USDT | +21.99% | $16,430,516.69 |
| DOS/USDT:USDT | +17.01% | $1,153,917.68 |
| NIULAI/USDT:USDT | +14.59% | $4,671,992.39 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NIULAI/USDT:USDT | below_1h_threshold | +2.97% | +2.98% |
| RE/USDT:USDT | below_1h_threshold | +2.64% | +2.65% |
| SOXS/USDT:USDT | below_1h_threshold | +2.28% | +2.29% |
| HEI/USDT:USDT | below_1h_threshold | +1.74% | +1.75% |
| DOT/USDT:USDT | below_1h_threshold | +1.03% | +1.04% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
