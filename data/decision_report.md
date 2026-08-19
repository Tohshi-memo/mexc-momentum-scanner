# Decision Report

- generated_at: 2026-08-19T09:41:19.566825+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11968**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11968, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.68%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.68% | **-0.68%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 15/20 | 75.0% | +0.12% | **+0.09%** |
| LIMIT_6PCT | 3/20 | 15.0% | -0.08% | **-0.01%** |
| LIMIT_5PCT | 3/20 | 15.0% | -0.70% | **-0.10%** |
| LIMIT_4PCT | 13/20 | 65.0% | -0.31% | **-0.20%** |
| LIMIT_BB3S | 2/15 | 13.3% | -1.80% | **-0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.28% | **+1.02%** |
| MARKET_LONG | 20/20 | 100.0% | +0.92% | **+0.92%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +1.16% | **+0.64%** |
| LIMIT_6PCT_LONG | 6/20 | 30.0% | +0.82% | **+0.24%** |
| LIMIT_2PCT_LONG | 10/20 | 50.0% | +0.24% | **+0.12%** |

## 2. $100 Live Portfolio

- 残高: **$121.29** / 初期 $100.00 (+21.29%)
- 確定トレード: 188件 (TP 72 / SL 111 / EXP 5)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.29
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$632.34** / 初期 $100.00 (+532.34%)
- 確定: 4229件 (Win 1301 / Loss 1378 / Flat 1550) / skip 4300件
- 成長率目線: 平均log +0.000436 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BTW/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $632.34

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.70** / 初期 $100.00 (+54.70%)
- 確定: 1821件 (Win 502 / Loss 428 / Flat 891) / skip 3558件
- 成長率目線: 平均log +0.000240 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0464 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: UNITREE/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.35% 残高後 $154.70

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.41** / 初期 $100.00 (+18.41%)
- 確定: 1745件 (Win 520 / Loss 662 / Flat 563) / pending 3件 / skip 1691件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000229 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BTW/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $118.41

## 6. Latest Market Context

- 更新: 2026-08-19T09:41:11.057494+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=64353.2
- Funnel: target 992 → liquid 176 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTW/USDT:USDT | +82.20% | $79,200,885.64 |
| UNITREE/USDT:USDT | +23.07% | $15,974,473.07 |
| HEMI/USDT:USDT | +22.61% | $3,038,319.11 |
| DOS/USDT:USDT | +14.94% | $1,075,217.94 |
| NIULAI/USDT:USDT | +11.42% | $4,790,365.56 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ACE/USDT:USDT | below_1h_threshold | +4.66% | +4.71% |
| BTW/USDT:USDT | below_1h_threshold | +4.63% | +4.69% |
| RE/USDT:USDT | below_1h_threshold | +1.89% | +1.95% |
| SKUU/USDT:USDT | below_1h_threshold | +1.46% | +1.52% |
| EDEN/USDT:USDT | below_1h_threshold | +1.35% | +1.41% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
