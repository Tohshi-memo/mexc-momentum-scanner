# Decision Report

- generated_at: 2026-07-25T10:51:20.826487+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9509**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.28% / filled 20/20。**
- 全期間 MARKET基準: n=9509, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.28%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.28% | **+0.28%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 8/20 | 40.0% | +1.43% | **+0.57%** |
| LIMIT_6PCT | 4/20 | 20.0% | +2.61% | **+0.52%** |
| MARKET | 20/20 | 100.0% | +0.28% | **+0.28%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +1.04% | **+0.26%** |
| LIMIT_BB3S | 6/18 | 33.3% | +0.52% | **+0.17%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.21% | **+0.91%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +3.98% | **+0.80%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.62% | **+0.55%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +0.67% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$104.82** / 初期 $100.00 (+4.82%)
- 確定トレード: 140件 (TP 47 / SL 88 / EXP 5)
- 最新: B2/USDT:USDT TP_HIT PnL +8.00% 残高後 $104.82
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$424.96** / 初期 $100.00 (+324.96%)
- 確定: 3338件 (Win 1052 / Loss 1082 / Flat 1204) / skip 2732件
- 成長率目線: 平均log +0.000433 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EUL/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $424.96

## 4. Robust Adaptive DryRun ($100)

- 残高: **$130.36** / 初期 $100.00 (+30.36%)
- 確定: 1165件 (Win 312 / Loss 254 / Flat 599) / skip 1755件
- 成長率目線: 平均log +0.000228 / 幾何平均 +0.023% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0347 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ACE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $130.36

## 5. Causal Adaptive DryRun ($100)

- 残高: **$105.59** / 初期 $100.00 (+5.59%)
- 確定: 556件 (Win 185 / Loss 215 / Flat 156) / pending 3件 / skip 420件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000354 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: B2/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $105.59

## 6. Latest Market Context

- 更新: 2026-07-25T10:51:14.058009+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=63996.7
- Funnel: target 897 → liquid 154 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DEXE/USDT:USDT | +76.37% | $98,080,086.55 |
| EUL/USDT:USDT | +65.98% | $6,213,759.70 |
| AKE/USDT:USDT | +27.68% | $50,502,147.80 |
| PROM/USDT:USDT | +16.00% | $3,984,339.42 |
| BANK/USDT:USDT | +9.04% | $78,661,974.77 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ANTHROPIC/USDT:USDT | below_1h_threshold | +3.51% | +3.47% |
| PONS/USDT:USDT | below_1h_threshold | +2.01% | +1.97% |
| SLX/USDT:USDT | below_1h_threshold | +1.85% | +1.81% |
| BEAT/USDT:USDT | below_1h_threshold | +1.49% | +1.44% |
| EUL/USDT:USDT | below_1h_threshold | +1.31% | +1.27% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
