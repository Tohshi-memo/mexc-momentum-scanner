# Decision Report

- generated_at: 2026-11-11T20:16:52.467485+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18698**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=18698, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.92%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.92% | **-0.92%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 9/20 | 45.0% | +2.06% | **+0.93%** |
| LIMIT_BB3S | 5/20 | 25.0% | +2.90% | **+0.73%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.57% | **+0.40%** |
| LIMIT_8PCT | 4/20 | 20.0% | +2.00% | **+0.40%** |
| LIMIT_9PCT | 4/20 | 20.0% | +2.00% | **+0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +2.35% | **+2.12%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +3.20% | **+1.60%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.60% | **+1.12%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.80% | **+1.08%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +2.86% | **+1.00%** |

## 2. $100 Live Portfolio

- 残高: **$120.89** / 初期 $100.00 (+20.89%)
- 確定トレード: 270件 (TP 97 / SL 165 / EXP 8)
- 最新: SNXX/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.89
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,734.29** / 初期 $100.00 (+1634.29%)
- 確定: 7230件 (Win 2083 / Loss 2313 / Flat 2834) / skip 8029件
- 成長率目線: 平均log +0.000395 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BTW/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $1,734.29

## 4. Robust Adaptive DryRun ($100)

- 残高: **$390.28** / 初期 $100.00 (+290.28%)
- 確定: 4779件 (Win 1283 / Loss 1057 / Flat 2439) / skip 7330件
- 成長率目線: 平均log +0.000285 / 幾何平均 +0.028% per trade / maxDD +4.29%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1234 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AGT/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $390.28

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6866件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000161 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-11T20:16:39.181251+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.27% price=74584.4
- Funnel: target 1103 → liquid 146 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AIN/USDT:USDT | +15.75% | $1,305,455.28 |
| Q/USDT:USDT | +12.69% | $2,632,477.27 |
| ARIA/USDT:USDT | +6.45% | $9,710,977.02 |
| AGT/USDT:USDT | +3.38% | $31,989,580.81 |
| ETHFI/USDT:USDT | +3.30% | $3,048,127.31 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SOXS/USDT:USDT | below_1h_threshold | +3.75% | +3.47% |
| SQQQ/USDT:USDT | below_1h_threshold | +1.33% | +1.06% |
| NIGHT/USDT:USDT | below_1h_threshold | +1.22% | +0.95% |
| ARIA/USDT:USDT | below_1h_threshold | +1.09% | +0.82% |
| ZRO/USDT:USDT | below_1h_threshold | +0.77% | +0.49% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
