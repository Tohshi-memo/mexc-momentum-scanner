# Decision Report

- generated_at: 2026-07-22T18:06:27.153467+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9303**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9303, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.22%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.22% | **-0.22%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 12/20 | 60.0% | +1.05% | **+0.63%** |
| LIMIT_BB3S | 4/18 | 22.2% | +1.25% | **+0.28%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.15% | **+0.13%** |
| LIMIT_5PCT | 4/20 | 20.0% | -0.29% | **-0.06%** |
| LIMIT_FIB1272 | 11/19 | 57.9% | -0.25% | **-0.15%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.66% | **+1.08%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.72% | **+0.65%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +0.98% | **+0.54%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.75% | **+0.52%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +0.64% | **+0.32%** |

## 2. $100 Live Portfolio

- 残高: **$105.37** / 初期 $100.00 (+5.37%)
- 確定トレード: 133件 (TP 45 / SL 83 / EXP 5)
- 最新: DEXE/USDT:USDT SL_HIT PnL -4.00% 残高後 $105.37
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$431.54** / 初期 $100.00 (+331.54%)
- 確定: 3290件 (Win 1039 / Loss 1059 / Flat 1192) / skip 2574件
- 成長率目線: 平均log +0.000444 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FWDISTOCK/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account -0.09% 残高後 $431.54

## 4. Robust Adaptive DryRun ($100)

- 残高: **$130.82** / 初期 $100.00 (+30.82%)
- 確定: 1160件 (Win 312 / Loss 253 / Flat 595) / skip 1554件
- 成長率目線: 平均log +0.000232 / 幾何平均 +0.023% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0360 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LAB/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $130.82

## 5. Causal Adaptive DryRun ($100)

- 残高: **$101.55** / 初期 $100.00 (+1.55%)
- 確定: 425件 (Win 142 / Loss 176 / Flat 107) / pending 3件 / skip 354件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000219 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BLESS/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $101.55

## 6. Latest Market Context

- 更新: 2026-07-22T18:06:19.117244+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=66031.2
- Funnel: target 890 → liquid 182 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BANK/USDT:USDT | +17.20% | $92,452,745.65 |
| BROCCOLIF3B/USDT:USDT | +9.73% | $1,601,738.15 |
| JIMOTHY/USDT:USDT | +6.23% | $3,267,905.75 |
| WLD/USDT:USDT | +4.79% | $34,645,664.56 |
| DEXE/USDT:USDT | +3.58% | $13,748,818.66 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BANK/USDT:USDT | below_1h_threshold | +4.76% | +4.71% |
| KIOXIASTOCK/USDT:USDT | below_1h_threshold | +0.93% | +0.87% |
| ZAMA/USDT:USDT | below_1h_threshold | +0.59% | +0.53% |
| USOIL/USDT:USDT | below_1h_threshold | +0.57% | +0.52% |
| NGAS/USDT:USDT | below_1h_threshold | +0.38% | +0.33% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
