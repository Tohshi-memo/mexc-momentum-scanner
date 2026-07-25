# Decision Report

- generated_at: 2026-07-25T11:11:16.549400+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9511**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.88% / filled 20/20。**
- 全期間 MARKET基準: n=9511, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.88%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.88% | **+0.88%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.88% | **+0.88%** |
| LIMIT_BB3S | 6/19 | 31.6% | +2.52% | **+0.80%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.43% | **+0.57%** |
| LIMIT_6PCT | 4/20 | 20.0% | +2.61% | **+0.52%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.32% | **+0.29%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +3.98% | **+0.80%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.88% | **+0.71%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +1.10% | **+0.33%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.31% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$104.82** / 初期 $100.00 (+4.82%)
- 確定トレード: 140件 (TP 47 / SL 88 / EXP 5)
- 最新: B2/USDT:USDT TP_HIT PnL +8.00% 残高後 $104.82
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$422.83** / 初期 $100.00 (+322.83%)
- 確定: 3339件 (Win 1052 / Loss 1083 / Flat 1204) / skip 2733件
- 成長率目線: 平均log +0.000432 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PROM/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $422.83

## 4. Robust Adaptive DryRun ($100)

- 残高: **$130.36** / 初期 $100.00 (+30.36%)
- 確定: 1165件 (Win 312 / Loss 254 / Flat 599) / skip 1757件
- 成長率目線: 平均log +0.000228 / 幾何平均 +0.023% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0738 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ACE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $130.36

## 5. Causal Adaptive DryRun ($100)

- 残高: **$105.68** / 初期 $100.00 (+5.68%)
- 確定: 558件 (Win 186 / Loss 216 / Flat 156) / pending 1件 / skip 420件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000346 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BEAT/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $105.68

## 6. Latest Market Context

- 更新: 2026-07-25T11:11:09.641403+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=64022.9
- Funnel: target 897 → liquid 150 → pre 50 → checked 49 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=1

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DEXE/USDT:USDT | +81.34% | $98,214,146.61 |
| EUL/USDT:USDT | +65.69% | $6,902,703.53 |
| AKE/USDT:USDT | +25.89% | $49,609,676.38 |
| PROM/USDT:USDT | +21.08% | $4,113,752.86 |
| BANK/USDT:USDT | +10.04% | $74,835,311.29 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEAT/USDT:USDT | below_1h_threshold | +2.92% | +2.95% |
| DEXE/USDT:USDT | below_1h_threshold | +2.69% | +2.72% |
| UB/USDT:USDT | below_1h_threshold | +2.16% | +2.19% |
| BASED/USDT:USDT | below_1h_threshold | +1.63% | +1.66% |
| BANK/USDT:USDT | below_1h_threshold | +0.90% | +0.92% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
