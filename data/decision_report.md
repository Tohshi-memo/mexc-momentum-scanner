# Decision Report

- generated_at: 2026-06-15T09:13:17.189363+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6767**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6767, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.91%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.91% | **-1.91%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.80% | **+0.28%** |
| LIMIT_10PCT | 2/20 | 10.0% | +0.73% | **+0.07%** |
| LIMIT_4PCT | 16/20 | 80.0% | -0.00% | **-0.00%** |
| LIMIT_5PCT | 8/20 | 40.0% | -0.29% | **-0.11%** |
| LIMIT_BB3S | 5/17 | 29.4% | -0.52% | **-0.15%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +2.58% | **+2.58%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +2.44% | **+1.96%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +2.03% | **+1.73%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +3.37% | **+1.52%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +2.33% | **+1.28%** |

## 2. $100 Live Portfolio

- 残高: **$103.02** / 初期 $100.00 (+3.02%)
- 確定トレード: 6件 (TP 4 / SL 2 / EXP 0)
- 最新: RIF/USDT:USDT TP_HIT PnL +8.00% 残高後 $103.02
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$178.94** / 初期 $100.00 (+78.94%)
- 確定: 1640件 (Win 429 / Loss 505 / Flat 706) / skip 1688件
- 成長率目線: 平均log +0.000355 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UAI/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $178.94

## 4. Robust Adaptive DryRun ($100)

- 残高: **$98.95** / 初期 $100.00 (-1.05%)
- 確定: 134件 (Win 26 / Loss 21 / Flat 87) / skip 44件
- 成長率目線: 平均log -0.000079 / 幾何平均 -0.008% per trade / maxDD +2.07%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_robust_growth_score) / robust_score -0.0102 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: UAI/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $98.95

## 5. Latest Market Context

- 更新: 2026-06-15T09:13:13.089622+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=65638.1
- Funnel: target 770 → liquid 143 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EVAA/USDT:USDT | +84.40% | $25,750,478.77 |
| ASTEROID/USDT:USDT | +68.53% | $4,288,315.07 |
| CLO/USDT:USDT | +40.53% | $2,232,383.09 |
| TRADOOR/USDT:USDT | +36.69% | $3,944,604.90 |
| H/USDT:USDT | +33.08% | $138,139,868.27 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FHE/USDT:USDT | below_1h_threshold | +3.91% | +3.89% |
| CLO/USDT:USDT | below_1h_threshold | +3.10% | +3.08% |
| UAI/USDT:USDT | below_1h_threshold | +2.05% | +2.03% |
| ASTEROID/USDT:USDT | below_1h_threshold | +1.79% | +1.77% |
| TRADOOR/USDT:USDT | below_1h_threshold | +1.47% | +1.44% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
