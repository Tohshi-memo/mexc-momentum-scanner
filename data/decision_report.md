# Decision Report

- generated_at: 2026-06-18T09:27:51.878675+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7032**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7032, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-0.33%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.33% | **-0.33%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 3/20 | 15.0% | +6.30% | **+0.95%** |
| LIMIT_9PCT | 3/20 | 15.0% | +5.72% | **+0.86%** |
| LIMIT_8PCT | 4/20 | 20.0% | +2.85% | **+0.57%** |
| LIMIT_ATR | 12/20 | 60.0% | +0.29% | **+0.17%** |
| LIMIT_BB3S | 4/18 | 22.2% | +0.05% | **+0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.13% | **+1.13%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.23% | **+1.04%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +2.35% | **+0.94%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.19% | **+0.77%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$100.97** / 初期 $100.00 (+0.97%)
- 確定トレード: 13件 (TP 5 / SL 8 / EXP 0)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.97
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$220.08** / 初期 $100.00 (+120.08%)
- 確定: 1878件 (Win 530 / Loss 597 / Flat 751) / skip 1715件
- 成長率目線: 平均log +0.000420 / 幾何平均 +0.042% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $220.08

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.53** / 初期 $100.00 (+7.53%)
- 確定: 305件 (Win 89 / Loss 83 / Flat 133) / skip 138件
- 成長率目線: 平均log +0.000238 / 幾何平均 +0.024% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0886 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $107.53

## 5. Latest Market Context

- 更新: 2026-06-18T09:27:43.461689+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.16% price=64268.9
- Funnel: target 793 → liquid 170 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| O/USDT:USDT | +69.08% | $4,360,082.07 |
| ESPORTS/USDT:USDT | +67.47% | $42,669,416.51 |
| SYN/USDT:USDT | +59.83% | $5,935,297.39 |
| HOME/USDT:USDT | +39.96% | $2,337,204.99 |
| FOLKS/USDT:USDT | +24.60% | $3,346,306.90 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BSB/USDT:USDT | below_1h_threshold | +3.51% | +3.67% |
| LAB/USDT:USDT | below_1h_threshold | +3.07% | +3.22% |
| XLM/USDT:USDT | below_1h_threshold | +2.26% | +2.42% |
| EVAA/USDT:USDT | below_1h_threshold | +1.92% | +2.08% |
| SIREN/USDT:USDT | below_1h_threshold | +1.63% | +1.78% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
